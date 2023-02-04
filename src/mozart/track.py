from .audio_clip import AudioClip
from typing import List, Dict
import dataclasses
import bisect
from gensound import Signal


@dataclasses.dataclass
class Timing:
    start_time: float
    duration: float

    @property
    def end_time(self) -> float:
        return self.start_time + self.duration

    def overlap(self, timing: "Timing") -> bool:
        return not (
            (
                timing.start_time <= self.start_time
                and timing.end_time <= self.start_time
            )
            or (timing.start_time >= self.end_time and timing.end_time >= self.end_time)
        )


class Track:
    def __init__(self):
        self.audio_track: Dict[AudioClip, Timing] = {}
        pass

    def _will_clash(self, timing: Timing) -> bool:
        keys: List[AudioClip] = sorted(
            list(self.audio_track.keys()), key=self.audio_track.get
        )
        key_i = (
            bisect.bisect_left(
                keys, timing.start_time, key=lambda x: self.audio_track[x].start_time
            )
            - 1
        )
        clip0 = self.audio_track[keys[key_i]]
        if clip0.overlap(timing):
            return True
        if key_i + 1 < len(keys):
            clip1 = self.audio_track[key_i + 1]
            if clip1.overlap(timing):
                return True
        return False

    def addClip(self, audio_clip: AudioClip, start_time: float, duration: float) -> int:
        self.audio_track[audio_clip] = Timing(start_time, duration)

    def play() -> "Track":
        pass

    def getSignal(self) -> "Signal":
        return Signal.concat([x.get_internal() for x in self.audio_track])

    def pause() -> "Track":
        pass
