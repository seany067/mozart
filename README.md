# mozart
You'll never guess what, he's back.

----

## Installing

`python setup.py install`

## How To Use

Each individual sound component of a song is contained within a subclass of `AudioClip`. Examples of such child classes include `DrumClip` for creating a drum machine from samples or a `SineSynth` which takes a list of notes/chords and sequentially plays them through a sine wave.

`AudioClip` objects can be sequentially played in a `Track` - specifying the start time and duration of each clip when adding it with the `add_clip` method. If you specify a duration > the length of the clip then it will repeat.

Multiple tracks can be played in parallel, much like tracks in a traditional DAW, through use of the `Session` object. A session can be created and tracks added through `add_track(track: Track)`. This will compile down the underlying gensound objects from each track into one `Audio` object to minimise timing problems (however this can become slow when clips contain lots of concatenation of audio components).

See examples like `tests/songs/lofi_beat.py` and `tests/songs/audio_effects.py` to get a greater idea on how the library works.

To use the visualiser, you first need to import `from mozart.wmp.player import start`. `start` is then a function that will take a `Signal` object, and will play and visualise the audio.