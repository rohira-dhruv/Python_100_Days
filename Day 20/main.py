# Snake Game Part-1
import time
from turtle import Screen
from snake import Snake

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game.")
snake = Snake()
is_game_on = True
screen.tracer(0)

screen.listen()

while is_game_on:
    screen.onkey(key="Up", fun=snake.up)
    screen.onkey(key="Down", fun=snake.down)
    screen.onkey(key="Left", fun=snake.left)
    screen.onkey(key="Right", fun=snake.right)
    snake.move()

    screen.update()
    time.sleep(0.1)

screen.exitonclick()
