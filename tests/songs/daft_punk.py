from mozart import SampleClip, Track, Session, Note, Pause
from mozart.drum_clip import DrumClip, DrumInstruments, DrumPatterns
from mozart.instrument.basic_synth import SquareSynth
from gensound.effects import Stretch
from gensound.transforms import FadeIn

dir = "resources/daft-punk/"

speed_up = 1.1

drum_kit = DrumClip(
    instruments=DrumInstruments(
        kick=dir + "kick.wav",
        kick2=dir + "kick.wav",
    ),
    patterns=DrumPatterns(
        tempo=129,
        kick=[1, 0, 1, 0] * 16,
        kick2=[1, 0, 1, 0] * 16,
    ),
)

somethings = SampleClip(dir + "somethings.wav").use_effects([2])

drum_track = Track()
drum_track.add_clip(drum_kit, 0e3, 60e03)
drum_track.use_effects([Stretch(speed_up)])

vocal_track = Track()
vocal_track.add_clip(somethings, 0e3, 60e03)
vocal_track.use_effects([FadeIn(10_000.0), Stretch(speed_up)])

session = Session()
session.add_track(drum_track)
session.add_track(vocal_track)


def test_song():
    session.get_signal().play(sample_rate=44100)


test_song()
