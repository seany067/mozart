from .track import Track, Timing
from .audio_clip import AudioClip
from typing import List
from gensound import Signal, Raw


class TrackMixer:
    def __init__(self):
        self._tracks: List[Track] = []

    def add_clip(self, audio_clip: AudioClip, timing: Timing) -> Track:
        for track in self._tracks:
            if track.will_clash(timing) is None:
                track.add_clip(audio_clip, timing.start_time, timing.duration)
                return track
        new_track = Track()
        new_track.add_clip(audio_clip, timing.start_time, timing.duration)
        self._tracks.append(new_track)
        return new_track

    def add_track(self, track: Track) -> Track:
        self._tracks.append(track)

    def play(self) -> Signal:
        signal = Signal()
        for track in self._tracks:
            signal += track.getSignal()
            signal = Raw(signal.mixdown(sample_rate=44100))
        signal.play()