from .basic_synth import BasicSynth
from ..note_chord import Note

from gensound import Square, ADSR, Sine, Gain, Raw
from gensound.effects import Vibrato


class PickSynth(BasicSynth):
    def instrument_builder(self, note: Note):
      adsr = ADSR(attack=0.004e3, decay=0.8e3, sustain=0.8, release=0.9e3)
      s = Sine(str(note), duration=note.duration)*Gain(-9)*adsr
      s += Sine(str(note)+"-1", duration=note.duration)*Gain(-9)*adsr
      s = Raw(s.mixdown(sample_rate=44100))
      s += Sine(str(note)+"+1", duration=note.duration)*Gain(-9)*adsr
      s = Raw(s.mixdown(sample_rate=44100))
      s += Square(str(note), duration=note.duration)*Gain(-50)*adsr
      s = Raw(s.mixdown(sample_rate=44100))
      s *= Vibrato(frequency=10, width=0.1)
      s = Raw(s.mixdown(sample_rate=44100))
      return s

      