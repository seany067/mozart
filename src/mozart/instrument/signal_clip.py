from mozart import AudioClip

from gensound.signals import Oscillator
from gensound.effects import Transform


class SignalClip(AudioClip):
    __internal: Oscillator

    def __init__(self, signal: Oscillator, duration: int, with_effects: list[Transform] = [], sample_rate=44100):
        self.__internal = signal
        self.clip_duration = duration
        self.with_effects = with_effects
        self.sample_rate = sample_rate

    def play(self):
        self.get_internal().play(sample_rate=self.sample_rate)

    def use_effects(self, effects: list[Transform] = []):
        return SignalClip(self.__internal, effects, self.sample_rate)

    def get_internal(self):
        transformed_internal = self.__internal
        for effect in self.with_effects:
            print("Applying effect", effect)
            transformed_internal *= effect

        transformed_internal.duration = self.clip_duration
        return transformed_internal
