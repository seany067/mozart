from .audio_clip import AudioClip
from gensound import WAV


class SampleClip(AudioClip):
    def __init__(self, filename: str, sample_rate: int = 44100):
        self.sample_rate = sample_rate
        self.__build_internal_representation(filename)

    def play(self):
        self.__internal.play(sample_rate=self.sample_rate)

    def __build_internal_representation(self, filename: str):
        self.__internal = WAV(filename)