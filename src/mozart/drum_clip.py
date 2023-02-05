from .audio_clip import AudioClip
from .wav import WAVWrapper
from gensound import Signal, Raw
from gensound.effects import Transform
from pathlib import Path


class DrumInstruments:
    __instruments: dict[str, str]

    def __init__(self, **kwargs: str):
        self.__instruments = kwargs

    def get_instruments(self):
        return self.__instruments


class DrumPatterns:
    __patterns: dict[str, list[float]]
    __tempo: int

    def __init__(self, tempo: int, **kwargs: list[float]):
        self.__patterns = kwargs
        self.__tempo = tempo

    def get_tempo(self):
        return self.__tempo

    def get_pattern(self):
        return self.__patterns


class DrumClip(AudioClip):
    __instruments: DrumInstruments
    __patterns: DrumPatterns

    def __init__(self, instruments: DrumInstruments, patterns: DrumPatterns):
        self.__instruments = instruments
        self.__patterns = patterns
        self.__build_internal_representation()

    def get_internal(self, with_effects: list[Transform] = []):
        transformed_internal = self.__internal
        for effect in with_effects:
            transformed_internal *= effect

        return transformed_internal

    def play(self, with_effects: list[Transform] = []):
        self.get_internal(with_effects).play()

    def __build_internal_representation(self):
        beat_length = 30e3 / float(self.__patterns.get_tempo())
        instruments = self.__instruments.get_instruments()
        patterns = self.__patterns.get_pattern()

        instrument_wav_map = {instrument: WAVWrapper(file) for instrument, file in instruments.items()}

        self.__internal = Signal()
        self.__internal += list(instrument_wav_map.values())[0] * 0

        for instrument, filename in instruments.items():
            for beat, attack in enumerate(patterns[instrument]):
                start_time = float(beat * beat_length)
                if attack:
                    self.__internal[start_time:] += instrument_wav_map[instrument]
                    self.__internal = self.__internal.mixdown(sample_rate=44100)
                    self.__internal = Raw(self.__internal)
