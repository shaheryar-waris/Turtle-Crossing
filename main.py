import time
import random
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)


cars = CarManager()
player = Player()
score = Scoreboard()

screen.listen()
screen.onkey(player.move_up,"w")
screen.onkey(player.move_down,"s")
screen.update()


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    cars.new_car()
    cars.move()
    screen.update()

    # no collision
    if player.ycor() == 280:
        score.score()
        player.update()
        cars.move_fast()

    #collision with the cars

    for x in cars.all_cars:
        if x.distance(player)<25:
            score.game_over()
            game_is_on = False


screen.exitonclick()

