from .audio_clip import AudioClip
from .exceptions import AudioClipOverlapException
from .wav import WAVWrapper
from pathlib import Path
from typing import Dict, Union, List, Tuple
from gensound import Signal, Silence, Sine
import dataclasses

SAMPLE_SOUND = WAVWrapper(str(Path(__file__).parent / "48_C_SyncLead_SP_01.wav"))
EMPTY_SOUND = SAMPLE_SOUND * 0


@dataclasses.dataclass(frozen=True)
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
        self.audio_track: Dict[AudioClip, List[Timing]] = {}

    def will_clash(self, timing: Timing) -> Union[Timing, None]:
        for timings in self.audio_track.values():
            for _timing in timings:
                if _timing.overlap(timing):
                    return _timing
        return None

    def add_clip(
        self, audio_clip: AudioClip, start_time: float, duration: float
    ) -> bool:
        timing = Timing(start_time, duration)
        if (clash_clip := self.will_clash(timing)) is not None:
            raise AudioClipOverlapException(f"{timing} will clash with {clash_clip}")
        if audio_clip in self.audio_track:
            self.audio_track[audio_clip].append(Timing(start_time, duration))
        else:
            self.audio_track[audio_clip] = [Timing(start_time, duration)]

    def list_clips(self) -> List[Tuple[Timing, AudioClip]]:
        timing_map: Dict[Timing, AudioClip] = {}
        for clip, timings in self.audio_track.items():
            for timing in timings:
                timing_map[timing] = clip
        sorted_clips = sorted(timing_map.items(), key=lambda x: x[0].start_time)
        return sorted_clips

    def _repeat_clip(self, clip: AudioClip, timing: Timing) -> Signal:
        clip_signal = Signal()
        clip_signal += EMPTY_SOUND
        repeat_count = round(timing.duration / clip.duration, ndigits=0)
        cur_time = 0.0
        for i in range(repeat_count):
            clip_signal = clip_signal | clip.get_internal()
            cur_time += clip.duration
        if cur_time < timing.duration:
            clip_signal = clip_signal | clip.get_internal()[:float(timing.duration - cur_time)]
        return clip_signal

    def getSignal(self) -> Signal:
        signal = Signal() | EMPTY_SOUND
        timing_map: Dict[Timing, AudioClip] = {}
        for clip, timings in self.audio_track.items():
            for timing in timings:
                timing_map[timing] = clip

        sorted_clips: List = sorted(timing_map.items(), key=lambda x: x[0].start_time)
        cur_time = 0.0
        for (timing, clip) in sorted_clips:
            clip_signal = clip.get_internal()
            if timing.duration > clip.duration:
                clip_signal = self._repeat_clip(clip, timing)
            if (timing.start_time > cur_time):
                signal = signal | (timing.start_time - cur_time)
            signal = signal | clip_signal[: timing.duration]
            cur_time = timing.end_time
        return signal

    def pause(self) -> "Track":
        return self
