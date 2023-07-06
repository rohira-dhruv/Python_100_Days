# Hirst Painting Project.
import random
import turtle
import colorgram
from turtle import Turtle, Screen

colors = colorgram.extract("hirst.jpg", 30)
rgb_colors = []
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    rgb_colors.append((r, g, b))

color_list = [(140, 176, 207), (25, 32, 48), (26, 107, 159), (237, 225, 235), (209, 161, 111), (144, 29, 63),
              (230, 212, 93), (4, 163, 197), (218, 60, 84), (229, 79, 43), (195, 130, 169), (54, 168, 114),
              (28, 61, 116), (172, 53, 95), (108, 182, 90), (110, 99, 87), (193, 187, 46), (240, 204, 2), (1, 102, 119),
              (19, 22, 21), (50, 150, 109), (172, 212, 172), (118, 36, 34), (221, 173, 188), (227, 174, 166),
              (153, 205, 220), (184, 185, 210)]


def set_random_color():
    new_color = random.choice(color_list)
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
turtle.colormode(255)

ypos = -225
for _ in range(10):
    timmy.setpos(-225, ypos)
    draw_dots()
    ypos += 50

my_screen = Screen()
my_screen.exitonclick()
