import pytest
from mozart import Track
from mozart.track import Timing
from mozart import AudioClip
from mozart.exceptions import AudioClipOverlapException

@pytest.fixture()
def track() -> Track:
    return Track()

def test_track_timings(track: Track):
    track.addClip(AudioClip(), 1, 3)
    assert track._will_clash(Timing(1.1, 1.8)) is not None
    assert track._will_clash(Timing(2, 1)) is not None
    assert track._will_clash(Timing(2, 1.1)) is not None
    assert track._will_clash(Timing(1, 1)) is not None
    assert track._will_clash(Timing(0.9, 1.1)) is not None

    assert track._will_clash(Timing(4, 1)) is None


def test_track_add_clip_throws(track: Track):
    track.addClip(AudioClip(), 1, 3)
    try:
        track.addClip(AudioClip(), 2, 1)
        assert False, "Exception should be thrown as the clips overlap"
    except AudioClipOverlapException as e:
        print(e)
        assert True, "Exception should be thrown as the clips overlap"