from .audio_clip import AudioClip
from .exceptions import AudioClipOverlapException
from typing import Dict, Union, List
from gensound import Signal, Silence
import dataclasses


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

    def addClip(
        self, audio_clip: AudioClip, start_time: float, duration: float
    ) -> bool:
        timing = Timing(start_time, duration)
        if (clash_clip := self._will_clash(timing)) is not None:
            raise AudioClipOverlapException(f"{timing} will clash with {clash_clip}")
        self.audio_track[audio_clip] = Timing(start_time, duration)

    def listClips(self) -> List[AudioClip]:
        return sorted(
            list(self.audio_track.keys()), key=lambda x: self.audio_track[x].start_time
        )

    def play(self) -> Signal:
        sorted_timings = sorted(
            list(self.audio_track.values()), key=lambda x: x.end_time
        )
        signal = Silence(duration=float(sorted_timings[-1].end_time))
        for clip, timing in self.audio_track.items():
            clip_signal = clip.get_internal()
            if timing.duration > clip.get_duration():
                clip_signal = Silence(duration=float(timing.duration))
                repeat_count = round(timing.duration / clip.get_duration(), ndigits=0)
                if timing.duration % clip.get_duration() != 0:
                    repeat_count += 1
                for i in range(repeat_count):
                    clip_signal[
                        float(i * timing.duration) : float(
                            (i * timing.duration) + timing.duration
                        )
                    ] += clip.get_internal()
            signal[float(timing.start_time) : float(timing.end_time)] += clip_signal
        return signal

    def pause(self) -> "Track":
        return self
