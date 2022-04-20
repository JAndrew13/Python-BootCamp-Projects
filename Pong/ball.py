from turtle import Turtle
import random
import time

SPEED = 10

class Ball(Turtle):

    def __init__(self):
        super().__init__()

        self.color("white")
        self.shape("circle")
        self.penup()
        self.x_move = 5
        self.y_move = 5
        self.setheading(random.randint(-60, 60))
        self.move_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        self.move_speed += 0.9

    def reset_position(self):
        self.hideturtle()
        self.goto(0,0)
        self.showturtle()
        time.sleep(1)
        self.bounce_x()
        self.move_speed = 0.1
