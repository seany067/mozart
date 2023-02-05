from mozart.note_chord import Note, Chord
from mozart.instrument.basic_synth import Sampler

# chorD = Chord([
#   Note("D3", duration=2e3),
#   Note("A3", duration=2e3),
#   Note("C4", duration=2e3),
#   Note("F#4", duration=2e3)
# ], duration=2e3)

# chorC = Chord([
#   Note("C3", duration=2e3),
#   Note("E3", duration=2e3),
#   Note("G3", duration=2e3),
#   Note("C4", duration=2e3),
#   Note("E4", duration=2e3)
# ], duration=2e3)

# chorAm = Chord([
#   Note("A2", duration=2e3),
#   Note("E3", duration=2e3),
#   Note("A3", duration=2e3),
#   Note("C4", duration=2e3),
#   Note("E4", duration=2e3)
# ], duration=2e3)

# chorF = Chord([
#   Note("F2", duration=2e3),
#   Note("C3", duration=2e3),
#   Note("F3", duration=2e3),
#   Note("A3", duration=2e3),
#   Note("C4", duration=2e3),
#   Note("F4", duration=2e3)
# ], duration=2e3)

# chorE = Chord([
#   Note("E2", duration=2e3),
#   Note("B2", duration=2e3),
#   Note("E3", duration=2e3),
#   Note("G#3", duration=2e3),
#   Note("B3", duration=2e3),
#   Note("E4", duration=2e3)
# ], duration=2e3)

# chorB7 = Chord([
#   Note("B2", duration=2e3),
#   Note("D#3", duration=2e3),
#   Note("A3", duration=2e3),
#   Note("B3", duration=2e3),
#   Note("F#4", duration=2e3)
# ], duration=2e3)

# chorA7 = Chord([
#   Note("A2", duration=2e3),
#   Note("E3", duration=2e3),
#   Note("G3", duration=2e3),
#   Note("C#4", duration=2e3),
#   Note("E4", duration=2e3)
# ], duration=2e3)

# chorDm = Chord([
#   Note("D3", duration=2e3),
#   Note("A3", duration=2e3),
#   Note("D4", duration=2e3),
#   Note("F4", duration=2e3)
# ], duration=2e3)

# chorGhm = Chord([
#   Note("G#2", duration=2e3),
#   Note("D#3", duration=2e3),
#   Note("G#3", duration=2e3),
#   Note("B3", duration=2e3),
#   Note("D#4", duration=2e3),
#   Note("G#4", duration=2e3)
# ], duration=2e3)

# chorB = Chord([
#   Note("C2", duration=2e3),
#   Note("F#3", duration=2e3),
#   Note("B3", duration=2e3),
#   Note("D#4", duration=2e3),
#   Note("F#4", duration=2e3)
# ], duration=2e3)

# chorFhm = Chord([
#   Note("F#2", duration=2e3),
#   Note("C#3", duration=2e3),
#   Note("F#3", duration=2e3),
#   Note("A3", duration=2e3),
#   Note("C#4", duration=2e3),
#   Note("F#4", duration=2e3)
# ], duration=2e3)

# chorBm = Chord([
#   Note("B2", duration=2e3),
#   Note("F#3", duration=2e3),
#   Note("B3", duration=2e3),
#   Note("D4", duration=2e3),
#   Note("F#4", duration=2e3)
# ], duration=2e3)

# chorCh7 = Chord([
#   Note("C#3", duration=2e3),
#   Note("D#3", duration=2e3),
#   Note("A3", duration=2e3),
#   Note("B3", duration=2e3),
#   Note("F#4", duration=2e3)
# ], duration=2e3)

# chorG = Chord([
#   Note("G2", duration=2e3),
#   Note("B2", duration=2e3),
#   Note("D3", duration=2e3),
#   Note("G3", duration=2e3),
#   Note("B3", duration=2e3),
#   Note("G4", duration=2e3)
# ], duration=2e3)

# chorA = Chord([
#   Note("A2", duration=2e3),
#   Note("E3", duration=2e3),
#   Note("A3", duration=2e3),
#   Note("C#4", duration=2e3),
#   Note("E4", duration=2e3)
# ], duration=2e3)


# chords = repeat(chor.with_shift, with_=[-1.6e3, -1.6e3, -1.7e3, -1.87e3, -1.6e3, -1.6e3, -1.6e3, -1.7e3, -1.87e3]) + \
#   repeat(chorD.with_shift, with_=[-1.6e3, -1.6e3, -1.6e3, -1.7e3, -1.87e3, -1.6e3, -1.6e3, -1.6e3, -1.7e3, -1.87e3]) + \
#   repeat(chorA.with_shift, with_=[-1.6e3, -1.6e3, -1.6e3, -1.7e3, -1.87e3]) + \
#   repeat(chor.with_shift, with_=[-1.6e3, -1.6e3, -1.6e3, -1.7e3, -1.87e3]) + \
#   repeat(chorD.with_shift, with_=[-1.6e3, -1.6e3, -1.6e3, -1.7e3, -1.87e3, -1.6e3, -1.6e3, -1.6e3, -1.7e3, -1.87e3])

#chordProgress= [chorG, chorG, chorD, chorD, chorA, chorG, chorD, chorD]

def createSong(lengths, notes):
  song = []
  for i in range(len(notes)):
    if (i) == 0:
      song.append(notes[i]) 
    else:
      song.append(notes[i].with_shift(lengths[0]))
  return song


chfilwyBar = [-1e3]
chfilwyProg = [Note("G4", duration=2e3), Note("A4", duration=1.5e3), Note("G4", duration=2e3), Note("E4", duration=3e3), 
               Note("G4", duration=2e3), Note("A4", duration=1.5e3), Note("G4", duration=2e3), Note("E4", duration=4e3),
               Note("G4", duration=2e3), Note("A4", duration=1.5e3), Note("G4", duration=2e3), Note("E4", duration=3e3), 
               Note("G4", duration=2e3), Note("A4", duration=1.5e3), Note("G4", duration=2e3), Note("E4", duration=4e3)]
chords = createSong(chfilwyBar, chfilwyProg)
pick = PickSynth(midi=chords)
pick.play()
