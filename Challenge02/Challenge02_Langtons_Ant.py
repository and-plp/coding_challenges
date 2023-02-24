
"""
Docstring:
Coding Challenge: Langton's Ant
"""

__author__ = 'Phil Palmer'
__version__ = '0.0.1'

import turtle

screen = turtle.Screen()
screen.bgcolor('yellow')
screen.screensize(10,10)

loc_col_map = {}

adam = turtle.Turtle()
adam.shape('square')
adam.shapesize(1)
adam.speed(100)
turtle.Screen().exitonclick()

step = 20
adam.forward(step)
adam.right(90)