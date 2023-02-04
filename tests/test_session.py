import math
import pytest
from mozart import Session
from mozart import Track
from mozart import AudioClip
from mozart import SampleClip
from gensound import test_wav


def test_session():
    track = Track()
    track.addClip(
        SampleClip(test_wav),
        start_time=0.0,
        duration=0.2e3,
    )
    session = Session()
    session.addTrack(track)
    sound = session.getSignal().realise(sample_rate=44100)
    assert math.isclose(sound.duration / 1000, 38.64705215419501)
