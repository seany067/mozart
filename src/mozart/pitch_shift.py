from gensound import Signal, Audio, Transform, Raw
from librosa.effects import pitch_shift as shift_pitch, time_stretch as stretch_time
from numpy import vstack



def pitch_shift(self: Signal, shift_by: int) -> Audio:
    mixed_signal = self.mixdown(sample_rate=44100)
    shifted_left = shift_pitch(mixed_signal.audio[0], 44100, shift_by)
    shifted_right = shift_pitch(mixed_signal.audio[1], 44100, shift_by)
    return Audio(sample_rate=44100).from_array(vstack((shifted_left, shifted_right)))


class PitchShift(Transform):
    def __init__(self, shift_by: int):
        self.shift_by = shift_by

    def realise(self, audio):
        shifter = Raw(pitch_shift(Raw(audio), self.shift_by))
        audio.audio[:, :] = shifter.audio[:, :]


def pitch_shift_single(self: Signal, shift_by: int) -> Audio:
    mixed_signal = self.mixdown(sample_rate=44100)
    shifted = shift_pitch(mixed_signal.audio[0], 44100, shift_by)
    return Audio(sample_rate=44100).from_array(shifted)


class PitchShiftSingle(Transform):
    def __init__(self, shift_by: int):
        self.shift_by = shift_by

    def realise(self, audio):
        shifter = Raw(pitch_shift_single(Raw(audio), self.shift_by))
        audio.audio[:, :] = shifter.audio[:, :]


def time_stretch(self: Signal, stretch_by: float) -> Audio:
    mixed_signal = self.mixdown(sample_rate=44100)
    shifted_left = stretch_time(mixed_signal.audio[0], stretch_by)
    shifted_right = shift_pitch(mixed_signal.audio[1], stretch_by)
    return Audio(sample_rate=44100).from_array(vstack((shifted_left, shifted_right)))


class TimeStretch(Transform):
    def __init__(self, shift_by: int):
        self.shift_by = shift_by

    def realise(self, audio):
        shifter = Raw(time_stretch(Raw(audio), self.shift_by))
        audio.audio[:, :] = shifter.audio[:, :]
