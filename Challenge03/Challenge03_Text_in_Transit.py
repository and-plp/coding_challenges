
"""
Docstring:
Coding Challenge: Text In Transit
"""

__author__ = 'Phil Palmer'
__version__ = '0.0.1'

import curses
import time

scrollText = "This is my example text to scroll across the screen"

def textScroller(screen):
    """Docstring: function to scroll text in curses wrapper"""    
    screen.addstr(scrollText)
    screen.getch()

curses.wrapper(textScroller)






    # scrollTextLength = len(scrollText)
    # for n in range(scrollTextLength):
    #     for n2 in range(width):
    #         position = (n+n2) % scrollTextLength
