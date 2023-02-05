from mozart.track import Track
from mozart.sample_clip import SampleClip
from gensound import WAV

dywm = SampleClip("dywm-bass.wav")

dywm_for_real = WAV("dywm-bass.wav")
(dywm_for_real | dywm_for_real | dywm_for_real).play()

track = Track()
track.add_clip(
    dywm,
    start_time=0.0,
    duration=0.5e3,
)
track.add_clip(
    dywm,
    start_time=0.5e3,
    duration=0.2e3,
)
track.add_clip(
    dywm,
    start_time=700,
    duration=0.5e3,
)

track.get_signal().play()
