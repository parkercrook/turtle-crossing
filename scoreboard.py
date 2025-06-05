import time
from turtle import Turtle

FONT = ("Courier", 24, "normal")
SCOREBOARD_POS = (-190, 230)
POINTS_POS = (190, 230)


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.setpos(SCOREBOARD_POS)
        self.level = 1
        self.write(f"Level: {self.level}", align="center", font=FONT)


    def next_level(self):
        self.level += 1
        self.clear()
        self.write(f"Level: {self.level}", align="center", font=FONT)


    def end_game(self):
        self.clear()
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)