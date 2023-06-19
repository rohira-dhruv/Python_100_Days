# Turtle Race Game.
import random
from turtle import Turtle, Screen

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []

ypos = -100
for color in colors:
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(color)
    new_turtle.penup()
    new_turtle.goto(-230, ypos)
    all_turtles.append(new_turtle)
    ypos += 40

if user_bet:
    is_race_on = True

while is_race_on:

    for current_turtle in all_turtles:

        if current_turtle.xcor() > 230:
            is_race_on = False
            winning_color = current_turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")
            break

        random_distance = random.randint(0, 10)
        current_turtle.forward(random_distance)
screen.exitonclick()
