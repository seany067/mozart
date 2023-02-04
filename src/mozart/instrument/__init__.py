from abc import abstractmethod
from typing import Union

from ..note_chord import Note, Chord, Pause

class Instrument:
    def __init__(self, midi: list[Union[Note, Chord, Pause]],
                 sample_rate: int = 44100):
        self.midi = midi
        self.sample_rate = sample_rate

    @abstractmethod
    def play(self):
        pass