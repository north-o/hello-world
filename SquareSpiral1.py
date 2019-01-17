"""
SquareSpiral1.py - Draws a square Spiral
"""

import turtle

turtle.bgcolor("black")
TurtlePen = turtle.Pen()

TurtlePen.pencolor("white")

for counter in range(100):
    TurtlePen.forward(counter)

    TurtlePen.left(90)

    if(counter > 50):
        turtle.bgcolor("red")
    else:
        turtle.bgcolor("green")
