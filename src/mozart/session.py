from typing import List
from gensound import Signal

from mozart.track import Track


class Session:
    def __init__(self):
        self.audio_session: List[Track] = []
        pass

    def add_track(self, track: Track):
        self.audio_session.append(track)

    def get_signal(self) -> "Signal":
        return Signal.mix(
            [track.get_signal() for track in self.audio_session]
        )  # type: ignore

    def play(self):
        self.get_signal().play()  # type: ignore
