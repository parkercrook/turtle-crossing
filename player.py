from turtle import Turtle

PLAYER_1_START_POSITION = (-150, -280)
PLAYER_2_START_POSITION = (150, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self, player_number):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.setheading(90)
        if player_number == "1":
            self.setpos(PLAYER_1_START_POSITION)
            self.color("light green")
        elif player_number == "2":
            self.setpos(PLAYER_2_START_POSITION)
            self.color("dark green")

    def move_forward(self):
        self.forward(5)

    def reset(self):
        self.setpos(PLAYER_1_START_POSITION)