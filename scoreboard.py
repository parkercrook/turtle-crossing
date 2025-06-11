from turtle import Turtle

LEVEL_FONT = ("Courier", 24, "normal")
SCORE_FONT = ("Courier", 18, "normal")
SCOREBOARD_POS = (-190, 230)
P1_POINTS_POS = (130, 230)
P2_POINTS_POS = (130, 200)


class Scoreboard(Turtle):

    def __init__(self, players):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.setpos(SCOREBOARD_POS)
        self.level = 0
        self.players = players
        self.next_level()

    def update_score(self):
        self.goto(P1_POINTS_POS)
        self.write(arg=f"Player {self.players[1].id} points: {self.players[1].points}", align="center", font=SCORE_FONT)
        self.goto(P2_POINTS_POS)
        self.write(arg=f"Player {self.players[2].id} points: {self.players[2].points}", align="center", font=SCORE_FONT)

    def add_point(self, player_id):
        self.players[player_id].points += 1

    def next_level(self):
        self.level += 1
        self.clear()
        self.goto(SCOREBOARD_POS)
        self.write(f"Level: {self.level}", align="center", font=LEVEL_FONT)
        self.update_score()


    def check_winner(self):
        for player in self.players.values():
            if player.points == 5:
                self.clear()
                self.goto(0, 0)
                self.write(f"PLAYER {player.id} WINS", align="center", font=LEVEL_FONT)
                return False
        return True