from turtle import Turtle
from random import Random

STARTING_MOVE_DISTANCE = 2
MOVE_INCREMENT = 1
RIGHT_SIDE_X_POS = 300
UPPER_CAR_BOUNDARY = 250
LOWER_CAR_BOUNDARY = -250
SPAWN_FREQ_INCREMENT = 2

def randomize_start_position():
    random = Random()
    y_pos = random.randint(LOWER_CAR_BOUNDARY, UPPER_CAR_BOUNDARY)
    return RIGHT_SIDE_X_POS, y_pos


class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.last_spawned_car = None
        self.active_cars = []
        self.spawn_car()
        self.car_speed = STARTING_MOVE_DISTANCE
        self.spawn_detection_pos = 250

    def spawn_car(self):
        car = Turtle()
        car.color("brown")
        car.shape("square")
        car.penup()
        car.setheading(180)
        car.shapesize(stretch_wid=1, stretch_len=2)
        car.goto(randomize_start_position())
        self.last_spawned_car = car
        self.active_cars.append(car)

    def check_spawn_again(self):
        if self.last_spawned_car is not None:
            if self.last_spawned_car.xcor() < self.spawn_detection_pos:
                self.spawn_car()

    def remove_inactive_cars(self):
        for car in self.active_cars:
            if car.xcor() < -350:
                self.active_cars.remove(car)

    def move_active_cars(self):
        for car in self.active_cars:
            car.forward(self.car_speed)

    def increase_difficulty(self):
        self.car_speed += MOVE_INCREMENT
        self.spawn_detection_pos += SPAWN_FREQ_INCREMENT

    def reset_speed(self):
        self.car_speed = STARTING_MOVE_DISTANCE

