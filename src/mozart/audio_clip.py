from abc import abstractmethod, ABC
from gensound import Signal
from gensound.effects import Transform


class AudioClip(ABC):
    __internal: Signal

    @abstractmethod
    def play(self):
        pass

    @abstractmethod
    def use_effects(self, effects: list[Transform] = []):
        pass

    @property
    def duration(self) -> float:
        internal = self.get_internal()
        if hasattr(internal, "duration"):
            return internal.duration
        if hasattr(internal, "audio") and hasattr(internal.audio, "duration"):
            return internal.audio.duration
        raise ValueError("Signal does not store a duration")

    def concat(self, clip: "AudioClip") -> Signal:
        return self.get_internal() | clip.get_internal()

    @abstractmethod
    def get_internal(self):
        pass
