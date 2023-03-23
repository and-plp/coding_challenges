
"""
Docstring:
Coding Challenge: Text In Transit
"""

__author__ = 'Phil Palmer'
__version__ = '0.0.1'

import curses
import time

interval = float(input("Scroll interval (Default = 0.1): ") or 0.1)
scrollRepetitions = int(input("Scroll count (Default = 20): ") or 20)
width = int(input("Text Width (Default = 25): ") or 25)

scrollText = (input("Text/String to scroll (Default = 'LoremIpsum'):") or "LoremIpsum")

def textScroller(screen):
    """Docstring: function to scroll text in curses wrapper"""    
    curses.curs_set(False)
    scrollTextLength = len(scrollText)
    for char in range((scrollRepetitions*scrollTextLength-width+1)):
        for space in range(width):
            curses.init_pair(1,curses.COLOR_BLUE,curses.COLOR_BLACK)
            curses.init_pair(2,curses.COLOR_RED,curses.COLOR_BLACK)
            BLUE_AND_BLACK = curses.color_pair(1)
            RED_AND_BLACK = curses.color_pair(2)
            screen.addstr(0,space,scrollText[((char + space) % scrollTextLength)],BLUE_AND_BLACK)
        screen.refresh()
        time.sleep(interval)
    screen.addstr(" Complete Press any key to exit ")
    screen.getch()


curses.wrapper(textScroller)






    # scrollTextLength = len(scrollText)
    # for n in range(scrollTextLength):
    #     for n2 in range(width):
    #         position = (n+n2) % scrollTextLength
