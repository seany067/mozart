import numpy as np
from gensound import Signal
from PySide6 import QtWidgets, QtCore, QtGui
from typing import Tuple, List
import math
import time
from ..wav import WAVWrapper

INTERVAL = 100


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
        self.controls = Controls(
            self.signal,
            [self.visualiser.start, lambda: self.threadpool.start(worker)],
            worker,
        )

        self.threadpool = QtCore.QThreadPool()

        self.layout.addWidget(self.visualiser)
        self.layout.addWidget(self.controls)


class Controls(QtWidgets.QWidget):
    def __init__(
        self, signal: Signal, play_callbacks: List, play_worker: PlayerWorker
    ) -> None:
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
    DEFAULT_HEIGHT = 800

    def __init__(self, signal: Signal, play_worker: PlayerWorker):
        super().__init__()
        self._colour_array_cache = None
        self.play_worker = play_worker
        self.sample_rate = 44100
        self.signal = signal
        self._size = (self.DEFAULT_HEIGHT, self.DEFAULT_HEIGHT)  # width, height
        self.seek = 0

        self.timer.setInterval(INTERVAL)
        self.timer.timeout.connect(self.update_image)

        self.layout = QtWidgets.QStackedLayout(self)
        self.label1 = QtWidgets.QLabel()
        self.label1.setScaledContents(True)
        self.layout.addWidget(self.label1)
        self.update_image()

    def resizeEvent(self, event: QtGui.QResizeEvent) -> None:
        self._size = (
            int((event.size().width() / event.size().height()) * self.DEFAULT_HEIGHT),
            self.DEFAULT_HEIGHT,
        )
        # self.update_image()
        return super().resizeEvent(event)

    def start(self) -> None:
        self.timer.start()

    @QtCore.Slot()
    def update_image(self) -> None:
        self.seek = (
            int((time.time() - self.play_worker.start) * self.sample_rate)
            if self.play_worker.start
            else 0
        )
        image = self.get_image()
        self.label1.setPixmap(QtGui.QPixmap(image))

    def get_image(self) -> QtGui.QImage:
        colour_array = self.get_colour_array()
        width, height = self._size
        colour_array = colour_array[int(self.seek) : int(self.seek + (width * 2))]
        c = (width // 2, height // 2)
        get_i = lambda w, h: int(math.sqrt(((w - c[0]) ** 2) + ((h - c[1]) ** 2)))
        high_dim_arr = np.array(
            [[colour_array[get_i(w, h)] for w in range(width)] for h in range(height)]
        )
        return QtGui.QImage(
            bytes(high_dim_arr),
            width,
            height,
            24 * width,
            QtGui.QImage.Format.Format_RGB888,
        )

    def get_colour_array(self) -> np.ndarray:
        if self._colour_array_cache is None:
            audio: np.ndarray = self.signal.audio.audio
            n = 512
            start_colour = np.array([0, 0, 255])
            end_colour = np.array([255, 0, 0])
            colour_range = np.round(
                np.array(
                    [
                        ((1 - (x / n)) * start_colour) + ((x / n) * end_colour)
                        for x in range(n)
                    ]
                )
            )

            arr = self._normalise_array(audio[0])
            self._colour_array_cache = [colour_range[int(i * (n - 1))] for i in arr]
        return self._colour_array_cache

    def _normalise_array(self, array: np.ndarray) -> np.ndarray:
        array = array.view(np.float64)
        v = np.interp(array, (array.min(), array.max()), (-1, +1))
        return np.abs(v)


def start(signal: Signal = None):
    app = QtWidgets.QApplication([])
    signal = signal or WAVWrapper(
        "/home/sean/mozart/gensound_temp_2023_02_05__06_11_13_pnrweyjr.wav"
    )
    widget = Player(signal)
    widget.resize(300, 300)
    widget.show()

    app.exec()
