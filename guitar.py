from mozart.note_chord import Note, Chord
from mozart.instrument.basic_synth import Sampler

chorD = Chord([
  Note("D3", duration=2e3),
  Note("A3", duration=2e3),
  Note("D4", duration=2e3),
  Note("F#4", duration=2e3)
], duration=2e3)

chorC = Chord([
  Note("C3", duration=2e3),
  Note("E3", duration=2e3),
  Note("G3", duration=2e3),
  Note("C4", duration=2e3),
  Note("E4", duration=2e3)
], duration=2e3)

chorAm = Chord([
  Note("A2", duration=2e3),
  Note("E3", duration=2e3),
  Note("A3", duration=2e3),
  Note("C4", duration=2e3),
  Note("E4", duration=2e3)
], duration=2e3)

chorF = Chord([
  Note("F2", duration=2e3),
  Note("C3", duration=2e3),
  Note("F3", duration=2e3),
  Note("A3", duration=2e3),
  Note("C4", duration=2e3),
  Note("F4", duration=2e3)
], duration=2e3)

chorEm = Chord([
  Note("E2", duration=2e3),
  Note("B2", duration=2e3),
  Note("E3", duration=2e3),
  Note("G3", duration=2e3),
  Note("B3", duration=2e3),
  Note("E4", duration=2e3)
], duration=2e3)

chorB7 = Chord([
  Note("B2", duration=2e3),
  Note("D#3", duration=2e3),
  Note("A3", duration=2e3),
  Note("B3", duration=2e3),
  Note("F#4", duration=2e3)
], duration=2e3)

chorA7 = Chord([
  Note("A2", duration=2e3),
  Note("E3", duration=2e3),
  Note("G3", duration=2e3),
  Note("C#4", duration=2e3),
  Note("E4", duration=2e3)
], duration=2e3)

chorDm = Chord([
  Note("D3", duration=2e3),
  Note("A3", duration=2e3),
  Note("D4", duration=2e3),
  Note("F4", duration=2e3)
], duration=2e3)

chorFhm = Chord([
  Note("F#2", duration=2e3),
  Note("C#3", duration=2e3),
  Note("F#3", duration=2e3),
  Note("A3", duration=2e3),
  Note("C#4", duration=2e3),
  Note("F#4", duration=2e3)
], duration=2e3)

chorBm = Chord([
  Note("B2", duration=2e3),
  Note("F#3", duration=2e3),
  Note("B3", duration=2e3),
  Note("D4", duration=2e3),
  Note("F#4", duration=2e3)
], duration=2e3)

chorCh7 = Chord([
  Note("C#3", duration=2e3),
  Note("D#3", duration=2e3),
  Note("A3", duration=2e3),
  Note("B3", duration=2e3),
  Note("F#4", duration=2e3)
], duration=2e3)

chorG = Chord([
  Note("G2", duration=2e3),
  Note("B2", duration=2e3),
  Note("D3", duration=2e3),
  Note("G3", duration=2e3),
  Note("B3", duration=2e3),
  Note("G4", duration=2e3)
], duration=2e3)

chorA = Chord([
  Note("A2", duration=2e3),
  Note("E3", duration=2e3),
  Note("A3", duration=2e3),
  Note("C#4", duration=2e3),
  Note("E4", duration=2e3)
], duration=2e3)


# chords = repeat(chor.with_shift, with_=[-1.6e3, -1.6e3, -1.7e3, -1.87e3, -1.6e3, -1.6e3, -1.6e3, -1.7e3, -1.87e3]) + \
#   repeat(chorD.with_shift, with_=[-1.6e3, -1.6e3, -1.6e3, -1.7e3, -1.87e3, -1.6e3, -1.6e3, -1.6e3, -1.7e3, -1.87e3]) + \
#   repeat(chorA.with_shift, with_=[-1.6e3, -1.6e3, -1.6e3, -1.7e3, -1.87e3]) + \
#   repeat(chor.with_shift, with_=[-1.6e3, -1.6e3, -1.6e3, -1.7e3, -1.87e3]) + \
#   repeat(chorD.with_shift, with_=[-1.6e3, -1.6e3, -1.6e3, -1.7e3, -1.87e3, -1.6e3, -1.6e3, -1.6e3, -1.7e3, -1.87e3])

Bar = [-1.6e3, -1.6e3, -1.6e3, -1.7e3, -1.87e3]

chordProgress= [chorG, chorG, chorD, chorD, chorA, chorG, chorD, chorD]

def createSong(bar, chordProg):
  chords = []
  for i in range(len(chordProg)):
    for j in range(len(bar)):
      if (i + j) == 0:
        chords.append(chordProg[i]) 
      else:
        chords.append(chordProg[i].with_shift(bar[j]))
  return chords

chfilwyBar = [-1.7e3, -1.7e3, -1.7e3, -1.7e3, -1.7e3, -1.7e3]
chfilwyProg = [chorC, chorG, chorAm, chorF, chorC, chorG, chorC, chorC, chorEm, chorF, chorC, chorG]
chords = createSong(chfilwyBar, chfilwyProg)
pick = Sampler("src/mozart/instrument/pluck.wav", Note("E2", 2e3), midi=chords)
pick.play()
