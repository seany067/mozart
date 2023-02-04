from .track import Track, Timing
from .audio_clip import AudioClip
from typing import List
from gensound import Signal


class TrackMixer:
    def __init__(self):
        self._tracks: List[Track] = []

    def add_clip(self, audio_clip: AudioClip, timing: Timing) -> None:
        for track in self._tracks:
            if track.will_clash(timing) is None:
                track.add_clip(audio_clip, timing.start_time, timing.duration)
                return
        new_track = Track()
        new_track.add_clip(audio_clip, timing.start_time, timing.duration)
        self._tracks.append(new_track)
        return

    def play(self) -> Signal:
        signal = Signal()
        for track in self._tracks:
            signal += track.play()
        signal.play()