from mozart import Note

from gensound import midC, Sine


#### vendored from gensound ####
def str_to_freq(f) -> float:  # this is a hack, better use regex or something else
    """'C##4+35' middle C## plus 35 cents
    'A' A4 (octave implied)
    """

    cents = 0
    if "+" in f:
        cents = int(f.split("+")[-1])
        f = f.split("+")[0]
    elif "-" in f:
        cents = -int(f.split("-")[-1])
        f = f.split("-")[0]

    semi = {"C": 0, "D": 2, "E": 4, "F": 5, "G": 7, "A": 9, "B": 11}[f[0]]
    f = f[1:]

    while len(f) > 0 and f[0] in ("#", "b"):
        semi += 1 if f[0] == "#" else -1
        f = f[1:]

    if len(f) > 0:
        semi += 12 * (int(f) - 4)  # octave

    return midC(semi + cents / 100)


def arpeggiator(
    base_note: Note,
    semis_range: int = 1,
    beats: int = 10,
    oscillator=Sine,
):
    base = str_to_freq(str(base_note))
    current = base
    sig = oscillator(base, base_note.duration)
    up = True
    for i in range(beats):
        if up:
            # increase current frequency by one semitone
            current *= 2 ** (1 / 12)
        else:
            # decrease current frequency by one semitone
            current /= 2 ** (1 / 12)
        # if we reached the end of the range, change direction
        if current > base * 2 ** (semis_range / 12) or current < base / 2 ** (
            semis_range / 12
        ):
            up = not up

        sig |= oscillator(current, base_note.duration)
    return sig
