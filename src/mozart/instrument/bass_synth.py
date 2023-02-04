from .basic_synth import BasicSynth
from ..note_chord import Note
from ..pitch_shift import pitch_shift_single

from gensound import Square, ADSR, Triangle, Sine, Raw
from gensound.transforms import FadeOut, FadeIn


class BassSynth(BasicSynth):
    def instrument_builder(self, note: Note):
        return (
            (
                Raw(
                    pitch_shift_single(
                        Sine(str(note), note.duration),
                        -4,
                    )
                )
                + Raw(
                    pitch_shift_single(
                        Sine(str(note), note.duration),
                        -3.75,
                    )
                )
                + Raw(
                    pitch_shift_single(
                        Triangle(str(note), note.duration),
                        -4,
                    )
                )
            )
            * FadeOut(0.025e3)
            * FadeIn(0.025e3)
        )  # * ADSR(0.0001e3, 0.3e3, 0.01e3, 0.2e3)
