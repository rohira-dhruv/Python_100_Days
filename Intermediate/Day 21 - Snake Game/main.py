# Snake Game
import time
from food import Food
from turtle import Screen
from snake import Snake
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game.")
snake = Snake()
is_game_on = True
screen.tracer(0)

food = Food()
score_board = ScoreBoard()

screen.listen()
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)

while is_game_on:
    screen.update()
    time.sleep(0.08)
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score_board.increase_score()

    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 270 or snake.head.ycor() < -290:
        is_game_on = False
        score_board.game_over()

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            is_game_on = False
            score_board.game_over()

screen.exitonclick()
