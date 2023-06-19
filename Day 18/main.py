import random
from turtle import Turtle, Screen


def set_random_color():
    new_color = (random.random(), random.random(), random.random())
    timmy.color(new_color)


def draw_dots():
    for _ in range(10):
        timmy.pendown()
        set_random_color()
        timmy.dot(20)
        timmy.penup()
        timmy.forward(50)


timmy = Turtle()
timmy.hideturtle()
timmy.speed("fastest")
timmy.penup()

ypos = -225
for _ in range(10):
    timmy.setpos(-225, ypos)
    draw_dots()
    ypos += 50

my_screen = Screen()
my_screen.exitonclick()
