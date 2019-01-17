"""
SquareSpiral1.py - Draws a square Spiral
"""

import turtle

#COLORS starting array
COLORS = ["red", "yellow", "blue", "green", "purple", "orange"]
turtle.bgcolor("black")
TurtlePen = turtle.Pen()

SIDES = 6

for counter in range(100):
    TurtlePen.pencolor(COLORS[counter%6])

    TurtlePen.forward(counter * 3/SIDES + counter)
    TurtlePen.left(360/SIDES + 1)
    TurtlePen.width(counter * SIDES/100)

    #TurtlePen.forward(counter)
    #TurtlePen.left(50)

    if(counter > 50):
        turtle.bgcolor("black")
    else:
        turtle.bgcolor("black")
