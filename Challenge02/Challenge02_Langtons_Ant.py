
"""
Docstring:
Coding Challenge: Langton's Ant
"""

__author__ = 'Phil Palmer'
__version__ = '0.0.1'

import turtle as t

def adam_loc(adam):
    """Docstring: function to return x,y coordinates of Adam"""
    return (round(adam.xcor()), round(adam.ycor()))

screen = t.Screen()
screen.bgcolor('white')
screen.screensize(500,500)

stamp_color_map = {}

adam = t.Turtle()
adam.shape('square')
adam.shapesize(1)
adam.speed(10)
distance = 20

loc = adam_loc(adam)

while True:

    if loc not in stamp_color_map or stamp_color_map[loc] == "white":

        adam.fillcolor("black")
        adam.stamp()
        stamp_color_map[adam_loc(adam)] = "black"
        adam.rt(90)
        adam.fd(distance)
        loc = adam_loc(adam)
        t.Screen().exitonclick()

    elif stamp_color_map[loc] == "black":

        adam.fillcolor("white")
        adam.stamp()
        stamp_color_map[adam_loc(adam)] = "white"
        adam.lt(90)
        adam.fd(distance)
        loc = adam_loc(adam)

        t.Screen().exitonclick()