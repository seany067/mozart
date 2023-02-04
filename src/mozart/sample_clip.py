from .audio_clip import AudioClip
from .wav import WAVWrapper
from gensound import WAV, Signal


class SampleClip(AudioClip):
    sample_rate: int

    def __init__(self, filename: str, sample_rate: int = 44100):
        self.sample_rate = sample_rate
        self.__build_internal_representation(filename)

    def get_internal(self):
        return self.__internal

    def play(self):
        self.__internal.play(sample_rate=self.sample_rate)

    def __build_internal_representation(self, filename: str):
        self.__internal = WAVWrapper(filename)
