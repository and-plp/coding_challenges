
"""
Docstring:
Coding Challenge: Control C, Control V
"""

__author__ = 'Phil Palmer'
__version__ = '0.0.1'

from pprint import pprint

# Original List of strigns.
s_list = [
    "the big red[CTRL+C] fox jumps over [CTRL+V] lazy dog.",
    "[CTRL+V]the tall oak tree towers over the lush green meadow.",
    "the sun shines down[CTRL+C] on [CTRL+V][CTRL+C] the busy [CTRL+V].",
    "[CTRL+V]the tall oak tree towers over the lush green meadow.",
    "a majestic lion[CTRL+C] searches for [CTRL+V] in the tall grass.",
    "the shimmering star[CTRL+X]Twinkling in the dark, [CTRL+V] shines bright.",
    "[CTRL+X]a fluffy white cloud drifts [CTRL+V][CTRL+C] across the sky, [CTRL+V]",
  ]

# List for new/processed strings.
s_list_new = []

def string_func(s):
    """
    Function to process [CTRL+C] [CTRL+V] [CTRL+X] commands within a string object
    """
    d1 = "[CTRL+C]"
    d1_pos = s.find(d1)
    d2 = "[CTRL+V]"
    d2_pos = s.find(d2)
    d3 = "[CTRL+X]"
    d3_pos = s.find(d3)

    while d1_pos != -1 or d2_pos != -1 or d3_pos != -1:
        if d1_pos == -1 and d3_pos == -1:
            s = s.replace(d2,'',1)
        elif d1_pos != -1:
            cp_val = s[0:d1_pos]
            s = s.replace(d1,'',1)
            s = s.replace(d2,cp_val,1)
        elif d3_pos != -1:
            cp_val = s[0:d3_pos]
            s = s[d3_pos:]
            s = s.replace(d3,'',1)
            s = s.replace(d2,cp_val,1)        
        d1_pos = s.find(d1)
        d2_pos = s.find(d2)
        d3_pos = s.find(d3)
    return(s)

# Iterate through strings within list and append processed string to new list.
for i, s in enumerate(s_list):
    s = string_func(s)
    s_list_new.append(s)

# Print new list.
pprint(s_list_new)
