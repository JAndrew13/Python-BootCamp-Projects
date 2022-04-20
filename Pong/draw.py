from turtle import Turtle

class Draw(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.speed("fastest")
        self.color("black")
        self.penup()
        self.width(5)
        self.pencolor("white")
        self.goto(0, 320)
        self.setheading(270)
        self.line()
        # self.border()

    def line(self):
        drawing = True
        while drawing:
            for distance in range(0, 13):
                self.pendown()
                self.forward(25)
                self.penup()
                self.forward(25)
            drawing = False
        self.border()

    def border(self):
        drawing = True
        self.setposition(-400, 400)
        while drawing:
            self.pendown()
            self.goto(-400, -400)
            self.goto(400, -400)
            self.goto(400, 400)
            self.goto(-400, 400)
            drawing = False

