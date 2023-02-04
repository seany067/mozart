from typing import Union

from .audio_clip import AudioClip
from instrument import Instrument
from .note_chord import Note, Chord, Pause


class MidiClip(AudioClip):
    def __init__(self, instrument: Instrument, midi: [Union[Note, Chord, Pause]]):
        self.instrument = instrument
        self.midi = midi

    def play(self):
        pass