"""
spiral_my_name.py - Spiral my name
"""



import turtle
turtle.bgcolor("blue")

colors = ["red", "yellow", "pink", "green", "purple", "orange"]

turtle_pen = turtle.Pen()

name = turtle.textinput("Enter your name.", "What is your name?!?! ")

for color_counter in range(100):
    turtle_pen.pencolor(colors[color_counter % 6])

    turtle_pen.penup()

    turtle_pen.forward(color_counter*4)

    turtle_pen.pendown()

    turtle_pen.write(name, font=("Comic Sans MS", int((color_counter+4)/4),"italic"))

    turtle_pen.left(92)