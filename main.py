import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.bgcolor("#0E86CC")
screen.title("Turtle Crossing")

car_manager = CarManager()
players = {
    1 : Player(1),
    2 : Player(2)
}
scoreboard = Scoreboard(players)

screen.onkeypress(players[1].move_forward, "w")
screen.onkeypress(players[2].move_forward, "Up")
screen.listen()

game_is_on = True
while game_is_on:
    time.sleep(0.025)
    screen.update()
    car_manager.check_spawn_again()
    car_manager.remove_inactive_cars()
    car_manager.move_active_cars()

    # Detect player collision with car and reset
    for car in car_manager.active_cars:
        if -20 < (car.xcor() - players[1].xcor()) < 20 and -20 < (car.ycor() - players[1].ycor()) < 22:
            players[1].reset()
        if -20 < (car.xcor() - players[2].xcor()) < 20 and -20 < (car.ycor() - players[2].ycor()) < 22:
            players[2].reset()

    # Detect level advancement
    if players[1].ycor() > 300:
        players[1].reset()
        scoreboard.add_point(1)
        scoreboard.next_level()
        car_manager.increase_difficulty()
    if players[2].ycor() > 300:
        players[2].reset()
        scoreboard.add_point(2)
        scoreboard.next_level()
        car_manager.increase_difficulty()

    game_is_on = scoreboard.check_winner()

screen.exitonclick()


