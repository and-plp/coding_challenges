
"""
Docstring:
Coding Challenge: Text In Transit
"""

__author__ = 'Phil Palmer'
__version__ = '0.0.1'

import curses
import time

width = 10
scrollText = "This is my example text to scroll across the screen"

def textScroller(screen):
    """Docstring: function to scroll text in curses wrapper"""    
    
    scrollTextLength = len(scrollText)
    
    for char in range(scrollTextLength):
        
        for space in range(5):
        
            screen.addstr(scrollText[char + space])
        
        screen.refresh()

        time.sleep(0.5)
    
    screen.getch()

curses.wrapper(textScroller)






    # scrollTextLength = len(scrollText)
    # for n in range(scrollTextLength):
    #     for n2 in range(width):
    #         position = (n+n2) % scrollTextLength
