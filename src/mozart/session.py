from typing import List
from gensound import Signal

from mozart.track import Track


class Session:
    def __init__(self):
        self.audio_session: List[Track] = []
        pass

    def add_track(self, track: Track):
        self.audio_session.append(track)

    def getSignal(self) -> "Signal":
        return Signal.mix(
            [track.getSignal() for track in self.audio_session]
        )  # type: ignore

    def play(self):
        self.getSignal().play()  # type: ignore
