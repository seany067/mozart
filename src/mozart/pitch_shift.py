from gensound import Signal, Audio
from librosa.effects import pitch_shift as shift_pitch, time_stretch as stretch_time
from numpy import vstack


def pitch_shift(self: Signal, shift_by: int) -> Audio:
    mixed_signal = self.mixdown(sample_rate=44100)
    shifted_left = shift_pitch(mixed_signal.audio[0], 44100, shift_by)
    shifted_right = shift_pitch(mixed_signal.audio[1], 44100, shift_by)
    return Audio(sample_rate=44100).from_array(vstack((shifted_left, shifted_right)))


def time_stretch(self: Signal, stretch_by: float) -> Audio:
    mixed_signal = self.mixdown(sample_rate=44100)
    shifted_left = stretch_time(mixed_signal.audio[0], stretch_by)
    shifted_right = shift_pitch(mixed_signal.audio[1], stretch_by)
    return Audio(sample_rate=44100).from_array(vstack((shifted_left, shifted_right)))
