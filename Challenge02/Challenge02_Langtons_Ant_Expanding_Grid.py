
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

def border_setup(border_l,distance,x,y):
    """Docstring: function to set the border line around Adam's field"""
    adam.penup()
    adam.shape('classic')
    adam.shapesize(1)
    adam.speed(10)    
    adam.setpos(x-distance/2,y-distance/2)
    adam.setheading(0)
    adam.pendown()
    adam.fd(border_l+distance)
    adam.lt(90)
    adam.fd(border_l+distance)
    adam.lt(90)
    adam.fd(border_l+distance)
    adam.lt(90)
    adam.fd(border_l+distance)

def new_border_setup(new_border_l,distance,new_x,new_y):
    """Docstring: function to set the border line around Adam's field""" 
    eve.penup()
    eve.shape('classic')
    eve.shapesize(1)
    eve.speed(10)    
    eve.setpos(new_x,new_y)
    eve.showturtle()
    eve.setheading(0)
    eve.pendown()
    eve.fd(new_border_l)
    eve.lt(90)
    eve.fd(new_border_l)
    eve.lt(90)
    eve.fd(new_border_l)
    eve.lt(90)
    eve.fd(new_border_l)
    eve.hideturtle()

def border_control(border_l,distance,x,y,return_loc):
    """Docstring: function to check if Adam is crossing the border line around the field"""    
    if x <= adam.xcor() <= border_l and y <= adam.ycor() <= border_l:
        return 1

    else:
        print("Border Breached")
        return 0

def new_border_control(new_border_l,distance,new_x,new_y,return_loc):
    """Docstring: function to check if Adam is crossing the border line around the field"""    
    if new_x <= adam.xcor() <= new_border_l and new_y <= adam.ycor() <= new_border_l:
        return 1

    else:
        print("New Border Breached")
        return 0

def langtons(border_l,distance,x,y):
    """Docstring: function to move Adam and invert field colours"""
    stamp_color_map = {}
    border_status = 1
    border_count = 1
    new_border_status = 1
    adam.penup()
    adam.setpos(border_l/2,border_l/2)
    adam.setheading(0)
    adam.shape('square')
    adam.pendown()
    loc = adam_loc(adam)

    while new_border_status==1:
        if loc not in stamp_color_map or stamp_color_map[loc] == "white":
            return_loc = adam.pos()
            if border_count == 1:
                border_status = border_control(border_l,distance,x,y,return_loc)
            elif border_count == 2:
                new_border_status = new_border_control(new_border_l,distance,new_x,new_y,return_loc)
            if border_status == 0 and border_count <2:
                new_border_setup(new_border_l,distance,new_x,new_y)
                border_count = border_count+1
            else:
                pass
            adam.fillcolor("black")
            adam.stamp()
            stamp_color_map[adam_loc(adam)] = "black"
            adam.rt(90)
            adam.fd(distance)
            loc = adam_loc(adam)
        elif stamp_color_map[loc] == "black":
            return_loc = adam.pos()
            if border_count == 1:
                border_status = border_control(border_l,distance,x,y,return_loc)
            elif border_count == 2:
                new_border_status = new_border_control(new_border_l,distance,new_x,new_y,return_loc)
            if border_status == 0 and border_count <2:
                new_border_setup(new_border_l,distance,new_x,new_y)
                border_count = border_count+1
            else:
                pass
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
new_border_l = border_l + (distance*3)
new_x = x - (distance*1.5)
new_y = y - (distance*1.5)

eve = t.Turtle()
eve.hideturtle()
adam = t.Turtle()
adam.screen.screensize(canvwidth=border_l, canvheight=border_l,bg="white")
border_setup(border_l,distance,x,y)
langtons(border_l,distance,x,y)
