import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()


screen.listen()
cars = []
screen.onkey(fun=player.move, key="Up")
i = 0
game_is_on = True
level = 1
scoreboard = Scoreboard()
while game_is_on:

    time.sleep(0.1)
    screen.update()
    if i % 6 == 0:
        car = CarManager()
        cars.append(car)
    for vehicle in cars:
        vehicle.move_car(level)
        if player.distance(vehicle) < 20:
            game_is_on = False
    if player.new_level():
        level += 1
        scoreboard.level_up()
    i += 1

screen.exitonclick()
