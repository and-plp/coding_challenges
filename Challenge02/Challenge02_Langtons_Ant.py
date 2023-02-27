
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

def langtons(border_l,distance,x,y):
    """Docstring: function to move Adam and invert field colours"""
    stamp_color_map = {}
    border_status = 1
    adam.penup()
    adam.speed(10000000)
    adam.setpos(border_l/2,border_l/2)
    adam.setheading(0)
    adam.shape('square')
    adam.pendown()
    loc = adam_loc(adam)

    while border_status==1:
        if loc not in stamp_color_map or stamp_color_map[loc] == "white":
            adam.fillcolor("black")
            adam.stamp()
            stamp_color_map[adam_loc(adam)] = "black"
            adam.rt(90)
            adam.fd(distance)
            loc = adam_loc(adam)
        elif stamp_color_map[loc] == "black":
            adam.fillcolor("white")
            adam.stamp()
            stamp_color_map[adam_loc(adam)] = "white"
            adam.lt(90)
            adam.fd(distance)
            loc = adam_loc(adam)

    t.exitonclick()



border_l = 200
x = 0.00
y = 0.00
distance = 20

adam = t.Turtle()
adam.screen.screensize(canvwidth=border_l, canvheight=border_l,bg="white")
langtons(border_l,distance,x,y)
