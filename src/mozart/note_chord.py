class Note:
    __string_rep: str

    def __init__(self, string_repr: str, duration: float, shift: float = 0):
        self.__string_rep = string_repr
        self.duration = duration
        self.shift = shift

    def __str__(self):
        return self.__string_rep

    def with_shift(self, shift: float) -> "Note":
        return Note(self.__string_rep, self.duration, shift)


class Chord:
    def __init__(self, notes: list[Note], duration: float, shift: float = 0):
        self.notes = notes
        self.duration = duration
        self.shift = shift

    @property
    def root_note(self):
        return self.notes[0]

    def with_shift(self, shift: float) -> "Chord":
        return Chord(self.notes, self.duration, shift)


class Pause:
    def __init__(self, duration: float):
        self.duration = duration
