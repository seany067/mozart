from mozart import SampleClip, Track, Session

dir = "resources/audio_effects/"
BPM = 130

def beats_to_duration(bpm: int, beats_to_run_for: float):
    return (60e3 / float(bpm)) * beats_to_run_for


drum_sample = SampleClip(dir+"130_BitJockey_SP_01.wav")
drum_track = Track()
drum_track.add_clip(drum_sample, 0.00, beats_to_duration(BPM, 32))


def test_audio_effects():
    session = Session()
    session.add_track(drum_track)
    session.get_signal().play(sample_rate=44100)
