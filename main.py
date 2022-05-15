import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()


player = Player()
car = CarManager()
scoreboard = Scoreboard()
screen.onkey(player.move, "Up")

speed_change = 1

game_is_on = True
while game_is_on:

    car.addCar()
    car.moveCars()

    # Detect New Level
    if player.ycor() > 280:
        scoreboard.increase_level()
        player.reset()
        player.clear()
        speed_change *= 0.8

    # Remove passed cars to save mem
    for i in car.cars:
        if i.xcor() > 350:
            car.cars.remove(i)

    # Detect Collision
        if i.distance(player) < 30:
            scoreboard.game_over()
            game_is_on = False



    time.sleep(0.1 * speed_change)
    screen.update()



screen.exitonclick()