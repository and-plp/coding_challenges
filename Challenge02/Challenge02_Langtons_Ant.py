
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

def border_setup(x,y,length):
    """Docstring: function to set the border line around Adam's field"""
    adam.penup()
    adam.shape('classic')
    adam.shapesize(1)
    adam.speed(10)    
    adam.setpos(x,y)
    adam.setheading(0)
    adam.pendown()
    adam.fd(length)
    adam.lt(90)
    adam.fd(length)
    adam.lt(90)
    adam.fd(length)
    adam.lt(90)
    adam.fd(length)

def border_control(border_l):
    """Docstring: function to check if Adam is crossing the border line around the field"""    
    if 0 <= adam.xcor() <= border_l and 0 <= adam.ycor() <= border_l:
        print("Border OK")

    else:
        print("Border Breached")



def langtons():
    """Docstring: function to move Adam and invert field colours"""
    adam.penup()    
    adam.setpos(200,200)
    adam.setheading(0)
    adam.shape('square')
    adam.pendown()
    loc = adam_loc(adam)

    while True:

        if loc not in stamp_color_map or stamp_color_map[loc] == "white":

            adam.fillcolor("black")
            adam.stamp()
            stamp_color_map[adam_loc(adam)] = "black"
            adam.rt(90)
            adam.fd(distance)
            loc = adam_loc(adam)
            print(loc)
            border_control(border_l)

        elif stamp_color_map[loc] == "black":

            adam.fillcolor("white")
            adam.stamp()
            stamp_color_map[adam_loc(adam)] = "white"
            adam.lt(90)
            adam.fd(distance)
            loc = adam_loc(adam)
            print(loc)
            border_control(border_l)


stamp_color_map = {}
border_l = 400
distance = 20
adam = t.Turtle()
adam.screen.screensize(canvwidth=400, canvheight=400,bg="white")

border_setup(0.00,0.00,border_l)

langtons()
