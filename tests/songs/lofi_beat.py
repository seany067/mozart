from mozart import SampleClip, Track, Session, Note, Pause
from mozart.drum_clip import DrumClip, DrumInstruments, DrumPatterns
from mozart.instrument.basic_synth import SquareSynth, SineSynth
from mozart.instrument.juno_synth import JunoSynth

dir = "resources/lofi_beat/"

drum_kit = DrumClip(
    instruments=DrumInstruments(
        kick_one=dir + "Kick_SP_01.wav",
        kick_two=dir + "Kick_SP_04.wav",
        snare_one=dir + "Snare_SP_05.wav",
        snare_two=dir + "Snare_SP_02.wav",
        hat=dir + "Hat_SP_11.wav",
    ),
    patterns=DrumPatterns(
        tempo=105,
        kick_one=   [1, 0, 0, 0] * 16,
        kick_two=   [1, 0, 0, 0] * 16,
        snare_one=  [0, 0, 1, 0] * 16,
        snare_two=  [0, 0, 1, 0] * 16,
        hat=        [0, 1, 0, 1] * 16
    )
)

vinyl_sample = SampleClip(dir + "Vinyl_Noise10.wav")

keys = SampleClip(dir + "COY_Panacea_Keys_105bpm_Bm.wav")


def beats_to_duration(bpm: int, beats_to_run_for: float):
    return (30e3 / float(bpm)) * beats_to_run_for


lead_synth = SineSynth(midi=[
    Note("B4", duration=beats_to_duration(105, 0.5)),
    Note("D4", duration=beats_to_duration(105, 0.5)),
    Note("G3", duration=beats_to_duration(105, 0.5)),
    Note("B4", duration=beats_to_duration(105, 0.5)),
    Note("D4", duration=beats_to_duration(105, 0.5)),
    Note("C#4", duration=beats_to_duration(105, 0.5)),
    Note("B4", duration=beats_to_duration(105, 0.5)),
    Note("B4", duration=beats_to_duration(105, 0.5)),
])

drum_track = Track()
drum_track.add_clip(drum_kit, 0.00, 60e03)

vinyl_track = Track()
vinyl_track.add_clip(vinyl_sample, 0.00, 60e03)

keys_track = Track()
keys_track.add_clip(keys, 0.00, 60e03)

lead_track = Track()
lead_track.add_clip(lead_synth, 0.00, 60e03)


def test_song():
    session = Session()
    session.add_track(drum_track)
    session.add_track(vinyl_track)
    session.add_track(keys_track)
    session.add_track(lead_track)
    session.get_signal().play(sample_rate=44100)
