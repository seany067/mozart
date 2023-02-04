import pytest
from mozart.drum_clip import DrumClip, DrumInstruments, DrumPatterns

@pytest.fixture()
def drum() -> DrumClip:
    return DrumClip(
        instruments=DrumInstruments(
            kick="eggs/kick1.wav",
            snare="eggs/snare1.wav",
            hihat="eggs/hat1.wav",
        ),
        patterns=DrumPatterns(
            tempo=116,
            kick=[1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0] * 3,
            snare=[0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0] * 3,
            hihat=[0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1] * 3,
        )
    )


def test_track_timings(drum: DrumClip):
    drum.play()
