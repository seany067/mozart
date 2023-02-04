import pytest
from mozart import Track
from mozart.track import Timing
from mozart import AudioClip

@pytest.fixture()
def track() -> Track:
    return Track()

def test_track_timings(track: Track):
    track.addClip(AudioClip(), 1, 3)
    assert track._will_clash(Timing(1.1, 1.8))
    assert track._will_clash(Timing(2, 1))
    assert track._will_clash(Timing(2, 1.1))
    assert track._will_clash(Timing(1, 1))
    assert track._will_clash(Timing(0.9, 1))

    assert not track._will_clash(Timing(4, 1))
