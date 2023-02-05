from .audio_clip import AudioClip
from .wav import WAVWrapper
from gensound.effects import Transform

class SampleClip(AudioClip):
    sample_rate: int

    def __init__(self, filename: str, sample_rate: int = 44100):
        self.sample_rate = sample_rate
        self.__build_internal_representation(filename)

    def get_internal(self, with_effects: list[Transform] = []):
        transformed_internal = self.__internal
        for effect in with_effects:
            transformed_internal *= effect

        return transformed_internal

    def play(self, with_effects: list[Transform] = []):
        self.get_internal(with_effects).play()

    def __build_internal_representation(self, filename: str):
        self.__internal = WAVWrapper(filename)
