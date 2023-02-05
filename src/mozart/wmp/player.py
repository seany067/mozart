import numpy as np
from gensound import Signal
from PySide6 import QtWidgets, QtCore, QtGui
from typing import Tuple, List
import math
import time
import librosa
from ..wav import WAVWrapper

INTERVAL = 200

def get_duration(signal) -> float:
    if hasattr(signal, "duration"):
        return signal.duration
    if hasattr(signal, "audio") and hasattr(signal.audio, "duration"):
        return signal.audio.duration
    raise ValueError("Signal does not store a duration")


class PlayerWorker(QtCore.QRunnable):

    def __init__(self, signal: Signal) -> None:
        super().__init__()
        self.signal = signal
        self.start = None
    
    @QtCore.Slot()
    def run(self) -> None:
        self.start = time.time()
        p = self.signal.play()


class Player(QtWidgets.QWidget):
    
    def __init__(self, signal: Signal) -> None:
        super().__init__()
        self.signal = signal
        self.layout = QtWidgets.QVBoxLayout(self)
        worker = PlayerWorker(self.signal)
        self.visualiser = Visualisation(self.signal, worker)
        self.controls = Controls(self.signal, [self.visualiser.start, lambda: self.threadpool.start(worker)], worker)

        self.threadpool = QtCore.QThreadPool()
        
        self.layout.addWidget(self.visualiser)
        self.layout.addWidget(self.controls)


class Controls(QtWidgets.QWidget):

    def __init__(self, signal: Signal, play_callbacks: List, play_worker: PlayerWorker) -> None:
        super().__init__()
        self.signal = signal
        self.play_worker = play_worker
        self.layout = QtWidgets.QVBoxLayout(self, alignment=QtCore.Qt.AlignCenter)
        self.play = QtWidgets.QPushButton("Play")
        self.stop = QtWidgets.QPushButton("Stop")
        self.layout.addWidget(self.play)

        self.play.clicked.connect(self.play_button)
        for callback in play_callbacks:
            self.play.clicked.connect(callback)

    @QtCore.Slot()
    def play_button(self):
        pass

    @QtCore.Slot()
    def stop_button(self):
        pass


class Visualisation(QtWidgets.QWidget):
    timer = QtCore.QTimer()
    DEFAULT_HEIGHT = 1000

    def __init__(self, signal: Signal, play_worker: PlayerWorker):
        super().__init__()
        self._colour_array_cache = None
        self.images = []
        self.play_worker = play_worker
        self.sample_rate = 44100
        self.signal = signal
        self._size = (self.DEFAULT_HEIGHT, self.DEFAULT_HEIGHT) # width, height
        self.seek = 0
        self.layout = QtWidgets.QStackedLayout(self)

        self.label = QtWidgets.QLabel()
        self.timer.setInterval(INTERVAL)
        self.timer.timeout.connect(self.update_image)
        
        self.build_images()
        if signal is not None:
            self.pixmap = QtGui.QPixmap(self.get_image())
            self.label.setPixmap(self.pixmap)
        self.label.setScaledContents(True)
        self.label.setSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        self.layout.addWidget(self.label)

    def resizeEvent(self, event: QtGui.QResizeEvent) -> None:
        self._size = (int((event.size().width() / event.size().height()) * self.DEFAULT_HEIGHT), self.DEFAULT_HEIGHT)
        self.update_image()
        return super().resizeEvent(event)

    def start(self) -> None:
        self.timer.start()

    def build_images(self) -> List[QtGui.QImage]:
        colour_array = self.get_colour_array()
        self.images = []
        width, height = self._size
        cache = {}
        def get_i(w, h):
            if (w, h) not in cache:
                cache[(w, h)] = int(math.sqrt(((w - (width // 2)) ** 2) + ((h - (height // 2)) ** 2)))
            return cache[(w, h)]
        
        def build_image(colour_array: np.ndarray):
            high_dim_arr = np.array([colour_array[get_i(w, h)] for w in range(width) for h in range(height)])
            return QtGui.QImage(bytes(high_dim_arr), width, height, 3*width, QtGui.QImage.Format.Format_RGB888)

        for i in np.arange(0, get_duration(self.signal) * self.sample_rate, INTERVAL * (self.sample_rate / 1000)):
            arr = colour_array[int(i):int(i+(width*height))]
            if arr.shape[0] == 0:
                break
            self.images.append(build_image(arr))

    def get_image(self) -> QtGui.QImage:
        return self.images[round(self.seek / (INTERVAL * (self.sample_rate / 1000)))]

    @QtCore.Slot()
    def update_image(self) -> None:
        self.seek = int((time.time() - self.play_worker.start) * self.sample_rate) if self.play_worker.start else 0
        self.label.setPixmap(QtGui.QPixmap(self.get_image()))

    def get_colour_array(self) -> np.ndarray:
        if self._colour_array_cache is None:
            audio: np.ndarray = self.signal.audio.audio
            arrays = [
                self._normalise_array(np.fft.fft(audio[0])),
                self._normalise_array(audio[0]),
                self._normalise_array(np.fft.ifft(audio[0])),
            ]
            self._colour_array_cache = np.array(list(zip(*arrays)))
        return self._colour_array_cache
    
    def _normalise_array(self, array: np.ndarray) -> np.ndarray:
        array = array.view(np.float64)
        v = np.interp(array, (array.min(), array.max()), (-1, +1))
        return np.round(np.abs((v * 255) % 255), 0)


def start(signal: Signal = None):
    app = QtWidgets.QApplication([])
    signal = signal or WAVWrapper("/home/sean/mozart/gensound_temp_2023_02_05__06_11_13_pnrweyjr.wav")
    widget = Player(signal)
    widget.resize(300, 300)
    widget.show()

    app.exec()