# Pong game.
import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("black")
screen.setup(width=1000, height=600)
screen.title("Pong Game")
screen.tracer(0)
is_game_on = True

left_paddle = Paddle((-450, 0))
right_paddle = Paddle((450, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(key="w", fun=left_paddle.up)
screen.onkey(key="s", fun=left_paddle.down)
screen.onkey(key="Up", fun=right_paddle.up)
screen.onkey(key="Down", fun=right_paddle.down)

while is_game_on:

    time.sleep(ball.move_speed)
    screen.update()

    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.xcor() > 480:
        scoreboard.l_point()
        ball.reset_position()

    if ball.xcor() < -480:
        scoreboard.r_point()
        ball.reset_position()

    if ball.distance(right_paddle) < 45 and ball.xcor() > 430 or ball.distance(left_paddle) < 45 and ball.xcor() < -430:
        ball.bounce_x()

    if scoreboard.l_score >= 5 or scoreboard.r_score >= 5:
        scoreboard.game_over()

screen.exitonclick()
