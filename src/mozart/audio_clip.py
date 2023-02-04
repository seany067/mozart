from abc import abstractmethod, ABC


class AudioClip(ABC):
    @abstractmethod
    def play(self):
        pass

