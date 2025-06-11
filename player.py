from turtle import Turtle
from randomcolor import RandomColor

PLAYER_1_START_POSITION = (-20, -280)
PLAYER_2_START_POSITION = (20, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
COLOR_GEN = RandomColor()


class Player(Turtle):

    def __init__(self, player_id):
        super().__init__()
        self.id = player_id
        self.shape("turtle")
        self.penup()
        self.setheading(90)
        self.points = 0
        self.color(COLOR_GEN.generate())
        if self.id == 1:
            self.goto(PLAYER_1_START_POSITION)
        elif self.id == 2:
            self.goto(PLAYER_2_START_POSITION)

    def move_forward(self):
        self.forward(5)

    def reset(self):
        if self.id == 1:
            self.setpos(PLAYER_1_START_POSITION)
        elif self.id == 2:
            self.setpos(PLAYER_2_START_POSITION)