import pytest
from pathlib import Path
from mozart import Track
from mozart.track import Timing
from mozart import AudioClip
from mozart.sample_clip import SampleClip
from mozart.exceptions import AudioClipOverlapException

FILE_DIR = Path(__file__).parent

@pytest.fixture()
def track() -> Track:
    return Track()

@pytest.fixture()
def sample_audio() -> AudioClip:
    return SampleClip(str(FILE_DIR / "48_C_SyncLead_SP_01.wav"))

def test_track_timings(track: Track, sample_audio: AudioClip) -> None:
    track.addClip(sample_audio, 1, 3)
    assert track._will_clash(Timing(1.1, 1.8)) is not None
    assert track._will_clash(Timing(2, 1)) is not None
    assert track._will_clash(Timing(2, 1.1)) is not None
    assert track._will_clash(Timing(1, 1)) is not None
    assert track._will_clash(Timing(0.9, 1.1)) is not None

    assert track._will_clash(Timing(4, 1)) is None


def test_track_add_clip_throws(track: Track, sample_audio: AudioClip) -> None:
    track.addClip(sample_audio, 1, 3)
    try:
        track.addClip(sample_audio, 2, 1)
        assert False, "Exception should be thrown as the clips overlap"
    except AudioClipOverlapException as e:
        print(e)
        assert True, "Exception should be thrown as the clips overlap"

def test_play(track: Track, sample_audio: AudioClip) -> None:
    track.addClip(sample_audio, 0, 2)
    track.addClip(sample_audio, 2, 2)
    track.addClip(sample_audio, 4, 2)
    track.play().play()