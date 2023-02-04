from .basic_synth import BasicSynth
from ..note_chord import Note

from gensound import Square, ADSR, Triangle


class JunoSynth(BasicSynth):
    def instrument_builder(self, note: Note):
        return (Square(str(note), note.duration) * ADSR(0.002e3, 0.3e3, 0.2, 0.2e3)) + Triangle(str(note), note.duration)