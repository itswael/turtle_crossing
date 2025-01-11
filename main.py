import time
from turtle import Turtle, Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=600, height=600)
scoreboard = Scoreboard()
player = Player()
car_manager = CarManager()

screen.tracer(0)

screen.listen()
screen.onkey(player.go_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    game_is_on = car_manager.detect_collision(player)
    if not game_is_on:
        scoreboard.game_over()
    if player.is_at_finish():
        scoreboard.level_up()
        player.moves_to_start()
        car_manager.level_up()


screen.exitonclick()