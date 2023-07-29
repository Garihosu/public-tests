# a small curses test in python

import curses

stdscr = curses.initscr()
curses.noecho()
curses.cbreak()

stdscr.addstr(0, 0, "hello weeb haha you thought i was gonna say world")
stdscr.refresh()
stdscr.getkey()

curses.endwin()
