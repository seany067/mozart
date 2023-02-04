import pytest
from pathlib import Path
from mozart.audio_clip import AudioClip
from mozart.sample_clip import SampleClip
from mozart.track import Timing
from mozart.track_mixer import TrackMixer


FILE_DIR = Path(__file__).parent

@pytest.fixture()
def sample_audio() -> AudioClip:
    return SampleClip(str(FILE_DIR / "48_C_SyncLead_SP_01.wav"))

def test_track_mixer(sample_audio: AudioClip):
    mixer = TrackMixer()
    mixer.add_clip(sample_audio, Timing(0, 2))
    mixer.add_clip(sample_audio, Timing(1, 2))
    mixer.add_clip(sample_audio, Timing(2, 2))
    assert len(mixer._tracks) == 2
