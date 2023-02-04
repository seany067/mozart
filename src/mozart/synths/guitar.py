from gensound import ADSR, Sine, Gain, Square
from gensound.effects import Vibrato

max_amplitude = 0
adsr = ADSR(attack=0.004e3, decay=0.6e3, sustain=0.5, release=0.9e3)
s = Sine("E", duration=2e3)*Gain(-9)*adsr
s += Sine("E-1", duration=2e3)*Gain(-9)*adsr
s += Sine("E+1", duration=2e3)*Gain(-9)*adsr
s += Square("E", duration=2e3)*Gain(-50)*adsr
s *= Vibrato(frequency=10, width=0.1)
s.play()