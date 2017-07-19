from turtle import *
import math

t = Turtle()

person = input('How many sides?')
sides = int(person)

setup(500,400)
x_pos = 0
y_pos = 0
t.setposition(x_pos, y_pos)

t.pendown()
for num in range(sides):
    print(num)
    t.forward(100)
    t.right(360/sides)


t.penup()
exitonclick()
