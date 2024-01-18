import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Crossing Project")
screen.tracer(0)
is_game_on = True

player = Player()
scoreboard = Scoreboard()
car_manager = CarManager()
screen.listen()
screen.onkey(key="Up", fun=player.move)

while is_game_on:
    time.sleep(0.1)
    screen.update()

    car_manager.generate_car()
    car_manager.move_cars()

    # Detect collision with car.
    for car in car_manager.cars:
        if car.distance(player) < 25:
            is_game_on = False
            scoreboard.game_over()

    # Detect successful crossing.
    if player.is_at_finish_line():
        player.go_to_start()
        car_manager.level_up()
        scoreboard.increase_level()

screen.exitonclick()
