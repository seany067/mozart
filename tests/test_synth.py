from mozart import SineSynth, Note, Chord, Pause

import numpy as np

from gensound import WAV, Raw, Audio
from gensound.effects import Stretch

from librosa.effects import pitch_shift

from mozart.instrument.basic_synth import SquareSynth, SawtoothSynth, TriangleSynth
from mozart.instrument.juno_synth import JunoSynth
from mozart.instrument.bass_synth import BassSynth

C_NOTE = Note("C3", duration=0.5e03)
E_NOTE = Note("E3", duration=0.5e03)
G_NOTE = Note("G3", duration=0.5e03)

PAUSE = Pause(duration=1e03)

C_CHORD = Chord([C_NOTE, E_NOTE, G_NOTE], duration=1e03)

MIDI = [
    PAUSE,
    C_NOTE,
    C_CHORD,
    PAUSE,
    E_NOTE,
    C_CHORD,
    PAUSE,
    G_NOTE,
    C_CHORD,
]


def test_sine_synth():
    synth = SineSynth(midi=MIDI)
    synth.play()


def test_square_synth():
    synth = SquareSynth(midi=MIDI)
    synth.play()


def test_sawtooth_synth():
    synth = SawtoothSynth(midi=MIDI)
    synth.play()


def test_triangle_synth():
    synth = TriangleSynth(midi=MIDI)
    synth.play()


def test_juno_synth():
    synth = JunoSynth(
        midi=[
            C_NOTE,
            E_NOTE,
            G_NOTE,
            E_NOTE,
            C_NOTE,
            G_NOTE,
            E_NOTE,
            E_NOTE,
            C_NOTE,
        ]
    )
    synth.play()


def test_bass_synth():
    synth = BassSynth(
        midi=[
            C_NOTE,
            E_NOTE,
            G_NOTE,
            E_NOTE,
            C_NOTE,
            G_NOTE,
            E_NOTE,
            E_NOTE,
            C_NOTE,
        ]
    )
    synth.play()


def test_shift_synth():
    C_NOTE = Note("C3", duration=2e3, shift=-1e3)
    D_NOTE = Note("D3", duration=2e3, shift=-1e3)
    E_NOTE = Note("E3", duration=2e3, shift=-1e3)

    synth = SawtoothSynth(
        midi=[
            Note("C3", duration=2e3),
            D_NOTE,
            E_NOTE,
            C_NOTE,
            D_NOTE,
            E_NOTE,
        ]
    )
    synth.play()
