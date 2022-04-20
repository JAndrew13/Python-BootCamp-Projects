from turtle import Screen
from paddle import Paddle
from scoreboard import Scoreboard
from ball import Ball
from draw import Draw
import time

P1_START = (350, 0)
P2_START = (-350, 0)
PLAYERS = 2

#load screen
screen = Screen()
screen.bgcolor("black")
screen.screensize(800, 800)
screen.title("JB's Pong Game")
screen.tracer()

#init + draw centerline tutle
draw = Draw()

#load OBJECTS
r_paddle = Paddle(P1_START)
l_paddle = Paddle(P2_START)
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(r_paddle.go_up, "Up")
screen.onkeypress(r_paddle.go_down, "Down")
screen.onkeypress(l_paddle.go_up, "w")
screen.onkeypress(l_paddle.go_down, "s")


#start game
game_is_on = True
while game_is_on:
    time.sleep(0.0001)
    screen.update()
    ball.move()

    #detect collision with wall
    if ball.ycor() > 380 or ball.ycor() < -380:
        ball.bounce_y()

    #detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()


    if ball.xcor() > 390:
        scoreboard.l_point()
        ball.reset_position()

    if ball.xcor() < -390:
        scoreboard.r_point()
        ball.reset_position()

#screen settings

screen.exitonclick()





