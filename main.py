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

player_1 = Player(player_number="1")
player_2 = Player(player_number="2")
car_manager = CarManager()
scoreboard = Scoreboard()

screen.onkeypress(player_1.move_forward, "w")
screen.onkeypress(player_2.move_forward, "Up")
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
        if -20 < (car.xcor() - player_1.xcor()) < 20 and -20 < (car.ycor() - player_1.ycor()) < 22:
            player_1.reset()
            scoreboard.end_game()
            game_is_on = False

    # Detect level advancement
    if player_1.ycor() > 300:
        player_1.reset()
        scoreboard.next_level()
        car_manager.increase_difficulty()

screen.exitonclick()


