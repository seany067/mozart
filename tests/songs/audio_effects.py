from mozart import SampleClip, Track, Session, arpeggiator, Note

from gensound import Gain, Triangle
from gensound.filters import SimpleLowShelf
from gensound.effects import OneImpulseReverb

from mozart.instrument.signal_clip import SignalClip

dir = "resources/audio_effects/"
BPM = 130


def beats_to_duration(bpm: int, beats_to_run_for: float):
    return (60e3 / float(bpm)) * (beats_to_run_for + 1)


drum_sample = SampleClip(dir+"130_BitJockey_SP_01.wav", with_effects=[
])
drum_track = Track()
drum_track.add_clip(drum_sample, 0.00, beats_to_duration(BPM, 32))

slurp_noise = SampleClip(dir+"slurp.wav", with_effects=[
    OneImpulseReverb(),
    Gain(-6)
])
slurp_track = Track()
slurp_track.add_clip(slurp_noise, 0.00, beats_to_duration(BPM, 32))

arp_synth = SignalClip(arpeggiator(
    Note("D3", duration=1e3), oscillator=Triangle
), int(beats_to_duration(BPM, 32)), with_effects=[
    Gain(-24)
])
arp_track = Track()
arp_track.add_clip(arp_synth, 0.00, beats_to_duration(BPM, 32))


def test_audio_effects():
    session = Session()
    session.add_track(drum_track)
    session.add_track(slurp_track)
    session.add_track(arp_track)
    session.get_signal().play(sample_rate=44100)
