from turtle import Turtle

SPEED = 5

class Player(Turtle):

#TURTLE INITIALIZE
    def __init__(self):
        super().__init__()
        #TURTLE INIT

        self.shape("turtle")
        self.color("black")
        self.penup()
        self.setheading(270)
        self.goto(0, -250)
        self.setheading(90)
        


# TURTLE MOVE UP/DOWN
    def go_up(self):
        new_y = self.ycor() + SPEED
        self.goto(self.xcor(), new_y)
    def go_down(self):
        new_y = self.ycor() - SPEED
        self.goto(self.xcor(), new_y)
    def go_left(self):
        new_x = self.xcor() - SPEED
        self.goto(new_x, self.ycor())
    def go_right(self):
        new_x = self.xcor() + SPEED
        self.goto(new_x, self.ycor())

        #TURTLE CONTROLS