from turtle import Turtle
FONT = ("Courier", 12, "normal")
FONT2 = ("Courier", 30, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.t_score = 0
        self.hideturtle()
        self.color("black")
        self.penup()
        self.goto(-190, 280)
        self.update_scoreboard()

    def score(self):
        self.t_score += 1
        self.clear()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score = {self.t_score} ", align="right", font=FONT)

    def game_over(self):
        self.penup()
        self.goto(0, 0)
        self.write("GAME -- OVER", align="center", font=FONT2)
