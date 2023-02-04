class Note:
    __string_rep: str

    def __init__(self, string_repr: str, duration: float):
        self.__string_rep = string_repr
        self.duration = duration

    def __str__(self):
        return self.__string_rep


class Chord:
    def __init__(self, notes: list[Note], duration: float):
        self.notes = notes
        self.duration = duration

    @property
    def root_note(self):
        return self.notes[0]


class Pause:
    def __init__(self, duration: float):
        self.duration = duration
