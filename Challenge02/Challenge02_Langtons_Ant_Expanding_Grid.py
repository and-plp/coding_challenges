
"""
Docstring:
Coding Challenge: Langton's Ant
"""

__author__ = 'Phil Palmer'
__version__ = '0.0.1'

import turtle as t

x = 0.00
y = 0.00
distance = 20
grid_sq = 10
border_length = distance*grid_sq


def grid_setup():
    adam.penup()
    adam.shape('classic')
    adam.shapesize(1)
    adam.speed(1000000)
    n = grid_sq+1
    grid_x=x
    grid_y=y

    for _ in range(n):
        adam.setpos(grid_x,y)
        adam.setheading(90)
        adam.pendown()
        adam.fd(border_length)
        grid_x = grid_x+distance
        adam.penup()
    for _ in range(n):
        adam.setpos(x,grid_y)
        adam.setheading(0)
        adam.pendown()
        adam.fd(border_length)
        grid_y = grid_y+distance
        adam.penup()

def new_grid_setup(border_length,distance,x,y):
    eve.penup()
    eve.shape('classic')
    eve.shapesize(1)
    eve.speed(1000000)
    n = grid_sq+3
    grid_x=x-distance
    grid_y=y-distance
    for _ in range(n):
        eve.setpos(grid_x,grid_y)
        eve.setheading(90)
        eve.pendown()
        eve.fd(border_length+distance*2)
        grid_x = grid_x+distance
        eve.penup()
    grid_x=x-distance
    grid_y=y-distance
    for _ in range(n):
        eve.setpos(grid_x,grid_y)
        eve.setheading(0)
        eve.pendown()
        eve.fd(border_length+distance*2)
        grid_y = grid_y+distance
        eve.penup()
    

def adam_loc(adam):
    """Docstring: function to return x,y coordinates of Adam"""
    return (round(adam.xcor()), round(adam.ycor()))

def border_control(border_length,x,y):
    """Docstring: function to check if Adam is crossing the border line around the field"""    
    if x <= adam.xcor() <= border_length and y <= adam.ycor() <= border_length:
        return 1
    else:
        print("Border Breached")
        return 0

def new_border_control(border_length,distance,x,y):
    """Docstring: function to check if Adam is crossing the border line around the field"""    
    new_border_l = border_length+distance*2
    new_x = x-distance
    new_y = y-distance
    if new_x <= adam.xcor() <= new_border_l and new_y <= adam.ycor() <= new_border_l:
        return 1
    else:
        print("New Border Breached")
        return 0

def langtons(distance):
    """Docstring: function to move Adam and invert field colours"""
    stamp_color_map = {}
    loc = adam_loc(adam)
    border_status = 1
    border_count = 1
    new_border_status = 1
    
    while new_border_status==1:

        if loc not in stamp_color_map or stamp_color_map[loc] == "white":
            return_loc = adam.pos()
            if border_count == 1:
                border_status = border_control(border_length,x,y)
            elif border_count == 2:
                new_border_status = new_border_control(border_length,distance,x,y)
            if border_status == 0 and border_count <2:
                new_grid_setup(border_length,distance,x,y)
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
            border_status = border_control(border_length,x,y)
            adam.fillcolor("white")
            adam.stamp()
            stamp_color_map[adam_loc(adam)] = "white"
            adam.lt(90)
            adam.fd(distance)
            loc = adam_loc(adam)

adam = t.Turtle()
adam.screen.screensize(canvwidth=border_length, canvheight=border_length,bg="white")
eve = t.Turtle()
eve.hideturtle()
grid_setup()
starting_coord = (border_length/2)-(distance/2)
adam.setpos(starting_coord,starting_coord)
adam.setheading(90)
adam.shape('square')
langtons(distance)
t.exitonclick()
