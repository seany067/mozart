from abc import abstractmethod, ABC
from gensound import Signal


class AudioClip(ABC):
    __internal: Signal
    @abstractmethod
    def play(self):
        pass

    def get_duration(self) -> float:
        if hasattr(self.get_internal(), "duration"):
            return self.get_internal().duration
        raise ValueError("Signal does not store a duration")

    def concat(self, clip: "AudioClip") -> Signal:
        return self.get_internal() | clip.get_internal()

    def get_internal(self):
        return self.__internal
