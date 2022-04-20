import turtle
import random

is_race_on = False

screen = Screen()


def replay(answer):
    if answer != "1":
        screen.bye()
    else:
        screen.clear()
        play()


def banner():
    banner_turtles = []
    banners_y = [150, -150]
    screen.bgcolor("black")
    for _ in range(0, 2):
        banner = Turtle(shape="turtle")
        banner.ht()
        banner_turtles.append(banner)
        banner.color("green")
        banner.speed("fastest")
        banner.penup()
        screen.bgcolor("pale green")
        banner.st()
        banner.setpos(-250, banners_y[_])
        banner.width(100)
        banner.pendown()
        banner.speed("slow")
        banner.goto(250, banners_y[_])


def play():
    screen.setup(width=500, height=400)

    screen.title("Turtle Racing!")
    banner()
    user_bet = screen.textinput(title="Place your bet!", prompt="Which turtle will win the race? Enter a color.\n"
                                                                "Red, Orange, Yellow, Blue, Green, or Purple")
    print(user_bet)
    colors = ["red", "orange", "yellow", "blue", "green", "purple"]
    y_positions = [-70, -40, -10, 20, 50, 80]
    all_turtles = []

    # Generate Racers
    for turtle_index in range(0, 6):
        new_turtle = Turtle(shape="turtle")
        new_turtle.color(colors[turtle_index])
        new_turtle.penup()
        new_turtle.goto(x=-230, y=y_positions[turtle_index])
        all_turtles.append(new_turtle)

    if user_bet:
        is_race_on = True

    while is_race_on:

        for turtle in all_turtles:

            rand_distance = random.randint(0, 10)
            turtle.forward(rand_distance)
            if turtle.xcor() > 230:
                is_race_on = False
                winning_color = turtle.pencolor()
                screen.bgcolor(winning_color)
                if winning_color == user_bet:
                    print("win")
                    answer = screen.textinput(title=f"{winning_color} was the winner!",
                                              prompt="Congrats, You Won!\n Would you like to play again? Enter '1' for YES or '2' for NO")
                else:
                    print("lose!")
                    answer = screen.textinput(title=f"{winning_color} was the winner!",
                                              prompt=f"Sorry, the {user_bet} turtle didn't win..\n Would you like to play again? Enter '1' for YES or '2' for NO")
                replay(answer)


play()
screen.exitonclick()
