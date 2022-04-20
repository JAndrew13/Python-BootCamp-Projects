from turtle import Turtle

DISTANCE = 20

class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.penup()
        self.goto(position)

    def go_up(self):
        new_y = self.ycor() + DISTANCE
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - DISTANCE
        self.goto(self.xcor(), new_y)


# starting_locations = [(380, 0)]
#
# PADDLE_LEGNTH = 3
# UP = 90
# DOWN = 270
# DISTANCE = 20
#
# class Paddle:
#     def __init__(self):
#         self.paddles = []
#         self.create_paddle()
#         self.r_control = self.paddles[0]
#
#     def create_paddle(self):
#             self.add_legnth(starting_locations[0])
#
#     def add_legnth(self, position):
#             self.paddle_bit = Turtle(shape="square")
#             self.paddle_bit.shapesize(stretch_len=5)
#             self.paddle_bit.color("white")
#             self.paddle_bit.setheading(90)
#             self.paddle_bit.penup()
#             self.paddle_bit.speed("fastest")
#             self.paddle_bit.goto(position)
#             self.paddles.append(self.paddle_bit)
#
#
#
#     def r_up(self):
#         self.r_control.forward(DISTANCE)
#
#     def r_down(self):
#         self.r_control.backward(DISTANCE)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~