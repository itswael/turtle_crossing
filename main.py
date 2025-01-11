import time
from turtle import Turtle, Screen
from player import Player
from car_manager import CarManager

player = Player()
screen = Screen()
car_manager = CarManager()
screen.setup(width=600, height=600)
screen.tracer(0)

screen.listen()
screen.onkey(player.go_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_cars()


screen.exitonclick()