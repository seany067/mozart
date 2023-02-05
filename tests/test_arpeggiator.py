from mozart import arpeggiator, Note
from gensound import Sine
import math


def test_arpeggiator():
    duration = (
        arpeggiator(Note("C3", 0.05e3), semis_range=4, beats=200, oscillator=Sine)
        .realise(44100)
        .duration
    )
    assert math.isclose(duration / 1000, 10)
