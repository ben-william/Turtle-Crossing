from turtle import Turtle
import random

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
POO_CHANCE = 2 # nominal representation of percentage i.e 100 gives 100% poo chance


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.color('black')
        self.shape('turtle')
        self.penup()
        self.setheading(90)
        self.reset()

    def move(self):
        self.forward(MOVE_DISTANCE)
        if random.randint(0,100) <= POO_CHANCE:
            for i in range (1,5):
                self.dot(3, 'brown')
                self.forward(1)

    def reset(self):
        self.goto(STARTING_POSITION)
