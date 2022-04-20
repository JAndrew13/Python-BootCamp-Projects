
from turtle import Turtle, Screen
from player import Player
from car import CarManager

import time


# init SCREEN
screen = Screen()
screen.setup(600, 600)
screen.title("JB's Crossy Road")
# upload BACKGROUND IMAGE
screen.bgpic("CR_bg.gif")
screen.tracer(0)

#SPAWN OBJECTS
player = Player()
car_manager = CarManager()



is_on = True
while is_on:
    time.sleep(0.01)
    screen.update()
    # ~~~~~~~~~~~~~~~~CODE~~~~~~~~~~~~~~~~#
    car_manager.create_car()
    car_manager.drive()

    if player.ycor() > 235:
        print("You Win!")
        is_on = False
    for car in car_manager.active_cars:
        if car.distance(player) < 20:
            is_on = False





   # ~~~~~~~~~~~~~~~~CODE~~~~~~~~~~~~~~~~~#
    screen.listen()
    screen.onkeypress(player.go_up, "Up")
    screen.onkeypress(player.go_down, "Down")
    screen.onkeypress(player.go_left, "Left")
    screen.onkeypress(player.go_right, "Right")


# screen EXIT
screen.exitonclick()
