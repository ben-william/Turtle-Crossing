from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
CAR_SPAWN_CHANCE = 10   # nominal representation of percentage i.e 100 gives 100% car chance


class CarManager:

    def __init__(self):
        self.cars = []

    def addCar(self):
        if random.randint(0, 100) <= CAR_SPAWN_CHANCE:
            new_car = Turtle()
            new_car.shape('square')
            new_car.shapesize(1, 2, 10)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            new_car.goto(-300, random.randint(-240, 240))
            self.cars.append(new_car)

    def moveCars(self):
        for car in self.cars:
            car.forward(MOVE_INCREMENT)


