from gensound import WAV
import shutil
import ffmpeg


class WAVWrapper(WAV):

    def __init__(self, filename):
        probe = ffmpeg.probe(filename)
        incorrect_format = False
        for stream_i in probe['streams']:
            if stream_i["sample_fmt"] != "s16":
                incorrect_format = True
                break
        if incorrect_format:
            temp_file = "temp_audio.wav"
            ffmpeg.input(filename).output(temp_file, ar=44100).overwrite_output().run()
            shutil.move(temp_file, filename)
        super().__init__(filename)

