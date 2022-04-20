from turtle import Turtle
import random
COLORS = ["red", "blue", "green", "purple", "pink", "black", "brown", "orange", "teal", "aquamarine", "violet", "yellow", "salmon"]
CAR_SP = 280
CAR_EP = -280
MIN_SPEED = 1
MAX_SPEED = 4
LANES = {
    1:(-200),
    2:(-155),
    3:(-105),
    4:(-50),
    5:(5),
    6:(55),
    7:(105),
    8:(155),
    9:(205)
}

class CarManager(Turtle):
    def __init__(self):
        self.active_cars = []
        self.create_car()

    def create_car(self):
        random_choice = random.randint(0,20)
        if random_choice == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            new_car.speed = random.randint(MIN_SPEED, MAX_SPEED)
            lane_num = random.randint(1, 9)
            new_y = LANES[lane_num]
            new_car.goto(CAR_SP, new_y)
            self.active_cars.append(new_car)

    def drive(self):
        for car in self.active_cars:
            car.backward(car.speed)





