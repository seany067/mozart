from gensound import Gain, Sine, Triangle, Sawtooth, Square, Silence, Raw
from typing import Union

from . import Instrument
from .. import Note, Chord, Pause


class BasicSynth(Instrument):
    def __init__(self, midi: list[Union[Note, Chord, Pause]], sample_rate: int = 44100):
        super().__init__(midi, sample_rate)
        self.__build_internal_representation()

    def play(self):
        self.__internal.play(sample_rate=self.sample_rate)

    def __build_internal_representation(self):
        self.__internal = Silence() * 0
        current_timestamp = 0.00

        for item in self.midi:
            if isinstance(item, Note):
                self.__internal[current_timestamp:current_timestamp + item.duration] += self.instrument_builder(item)
            elif isinstance(item, Chord):
                chord = self.instrument_builder(item.root_note)
                for note in item.notes[1:]:
                    chord += self.instrument_builder(note)

                self.__internal[current_timestamp:current_timestamp + item.duration] += chord
                self.__internal = self.__internal.mixdown(sample_rate=self.sample_rate)
                self.__internal = Raw(self.__internal)

            current_timestamp += item.duration

        self.__internal *= Gain(-12)


class SineSynth(BasicSynth):
    def instrument_builder(self, note: Note):
        return Sine(str(note), note.duration)


class SquareSynth(BasicSynth):
    def instrument_builder(self, note: Note):
        return Square(str(note), note.duration)


class SawtoothSynth(BasicSynth):
    def instrument_builder(self, note: Note):
        return Sawtooth(str(note), note.duration)


class TriangleSynth(BasicSynth):
    def instrument_builder(self, note: Note):
        return Triangle(str(note), note.duration)