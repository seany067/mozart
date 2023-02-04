from .audio_clip import AudioClip
from .exceptions import AudioClipOverlapException
from typing import List, Dict, Union
import dataclasses
import bisect

@dataclasses.dataclass
class Timing:
    start_time: float
    duration: float

    @property
    def end_time(self) -> float:
        return self.start_time + self.duration

    def overlap(self, timing: 'Timing') -> bool:
        return not (
            (timing.start_time <= self.start_time and timing.end_time <= self.start_time) or
            (timing.start_time >= self.end_time and timing.end_time >= self.end_time)
        )

    def __str__(self) -> str:
        return f"{self.start_time}---{self.end_time}"

class Track:

    def __init__(self):
        self.audio_track: Dict[AudioClip, Timing] = {}

    def _will_clash(self, timing: Timing) -> Union[AudioClip, None]:
        for clip, _timing in self.audio_track.items():
            if _timing.overlap(timing):
                return clip
        return None
        
    def addClip(self, audio_clip: AudioClip, start_time: float, duration: float) -> bool:
        timing = Timing(start_time, duration)
        if (clash_clip := self._will_clash(timing)) is not None:
            raise AudioClipOverlapException(f"{timing} will clash with {clash_clip}")
        self.audio_track[audio_clip] = Timing(start_time, duration)

    def play() -> 'Track':
        pass

    def pause() -> 'Track':
        pass