from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5

class CarManager():
    def __init__(self):
        self.all_cars=[]
        self.speed = STARTING_MOVE_DISTANCE

    def new_car(self):
        chance = random.randint(1,6)
        if chance == 1:
            new_car = Turtle('square')
            new_car.shapesize(stretch_len=2, stretch_wid=1)
            new_car.color(random.choice(COLORS))
            y = random.randint(-250, 250)
            new_car.penup()
            new_car.goto(300, y)
            self.all_cars.append(new_car)

    def move(self):
        for car in self.all_cars:
            car.backward(self.speed)

    def move_fast(self):
        self.speed += MOVE_INCREMENT




