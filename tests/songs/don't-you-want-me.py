from mozart.instrument.basic_synth import Sampler
from mozart import Note

# dywm = SampleClip("dywm-bass.wav")

Sampler(
    "resources/don't-you-want-me/dywm-bass.wav",
    Note("A2", 0.5e3),
    midi=[
        Note("A1", 0.5e3),
        Note("A1", 0.5e3),
        Note("E1", 0.25e3),
        Note("G1", 0.25e3),
        Note("A1", 0.5e3),
        Note("A1", 0.25e3),
        Note("E1", 0.25e3),
        Note("G1", 0.25e3),
        Note("C2", 0.5e3),
        Note("A1", 0.5e3),
        Note("A1", 0.5e3),
        Note("E1", 0.25e3),
        Note("G1", 0.25e3),
        Note("A1", 0.5e3),
    ],
).play()
