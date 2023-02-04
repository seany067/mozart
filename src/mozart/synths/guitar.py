from gensound import ADSR, Sine, Gain, Square
from gensound.effects import Vibrato, Stretch
from gensound.transforms import Shift
import time

#max_amplitude = 0
#adsr = ADSR(attack=0.004e3, decay=0.6e3, sustain=0.5, release=0.9e3)
#s = Sine("E", duration=2e3)*Gain(-9)*adsr
#s += Sine("E-1", duration=2e3)*Gain(-9)*adsr
#s += Sine("E+1", duration=2e3)*Gain(-9)*adsr
#s += Square("E", duration=2e3)*Gain(-50)*adsr
#s *= Vibrato(frequency=10, width=0.1)
#s.play()


def Pick(note):
  adsr = ADSR(attack=0.004e3, decay=0.6e3, sustain=0.5, release=0.9e3)
  s = Sine(note, duration=2e3)*Gain(-9)*adsr
  s += Sine(note+"-1", duration=2e3)*Gain(-9)*adsr
  s += Sine(note+"+1", duration=2e3)*Gain(-9)*adsr
  s += Square(note, duration=2e3)*Gain(-50)*adsr
  s *= Vibrato(frequency=10, width=0.1)
  return s

def makeChord(note):
  d = Pick(note[0])
  for i in range(1, len(note)):
    d += Pick(note[i])
  return d


d = (Pick("D3")[0.3e3:] + Pick("A3")[0.3e3:] + Pick("D4")[0.3e3:] + Pick("F#4"))
chorD = makeChord(["D3","A3","D4","F#4"])
chor = makeChord(["G2","B2","D3","G3","B3","G4"])
chorA = makeChord(["A2","E3","A3","C#4","E4"])
(chor | (chor * Shift(-1.6e3)) | (chor * Shift(-1.6e3)) | (chor * Shift(-1.7e3)) | (chor * Shift(-1.87e3)) |
 (chor * Shift(-1.6e3)) | (chor * Shift(-1.6e3)) | (chor * Shift(-1.6e3)) | (chor * Shift(-1.7e3)) | (chor * Shift(-1.87e3)) |
 (chorD * Shift(-1.6e3)) | (chorD * Shift(-1.6e3)) | (chorD * Shift(-1.6e3)) | (chorD * Shift(-1.7e3)) | (chorD * Shift(-1.87e3)) |
 (chorD * Shift(-1.6e3)) | (chorD * Shift(-1.6e3)) | (chorD * Shift(-1.6e3)) | (chorD * Shift(-1.7e3)) | (chorD * Shift(-1.87e3)) |
 (chorA * Shift(-1.6e3)) | (chorA * Shift(-1.6e3)) | (chorA * Shift(-1.6e3)) | (chorA * Shift(-1.7e3)) | (chorA * Shift(-1.87e3)) |
 (chor * Shift(-1.6e3)) | (chor * Shift(-1.6e3)) | (chor * Shift(-1.6e3)) | (chor * Shift(-1.7e3)) | (chor * Shift(-1.87e3)) |
 (chorD * Shift(-1.6e3)) | (chorD * Shift(-1.6e3)) | (chorD * Shift(-1.6e3)) | (chorD * Shift(-1.7e3)) | (chorD * Shift(-1.87e3)) |
 (chorD * Shift(-1.6e3)) | (chorD * Shift(-1.6e3)) | (chorD * Shift(-1.6e3)) | (chorD * Shift(-1.7e3)) | (chorD * Shift(-1.87e3))).play()