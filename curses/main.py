# a small curses test in python

import curses

stdscr = curses.initscr()
curses.noecho()
curses.cbreak()

stdscr.printw("hello weeb haha you thought i was gonna say world")
stdscr.refresh()
stdscr.getkey()

curses.endwin()
