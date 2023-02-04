from gensound import WAV, test_wav, Sine
import curses
from curses import wrapper


# little interactive program to play notes
def main(stdscr):
    curses.cbreak()

    stdscr.clear()
    stdscr.addstr(0, 0, "play some notes! [A-G]. use q to quit")

    stdscr.refresh()
    while key := stdscr.getkey():
        if key == "q":
            break
        else:
            stdscr.addstr(1, 0, key)
            stdscr.refresh()
            s = Sine(key, duration=0.2e3)
            s.play()
            curses.flushinp()


wrapper(main)
