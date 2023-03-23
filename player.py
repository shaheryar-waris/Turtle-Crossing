from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.create_player()


    def create_player(self):
        self.setheading(90)
        self.shape("turtle")
        self.penup()
        self.goto(0, -280)

    def move_up(self):
        if self.ycor() < FINISH_LINE_Y:
            self.forward(MOVE_DISTANCE)

    def move_down(self):
        if self.ycor() > -300:
            self.backward(MOVE_DISTANCE)

    def update(self):
        self.penup()
        self.goto(0, -280)




