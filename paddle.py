from turtle import Turtle

Y_POSITION = [-40, -20, 0, 20, 40]
UP = 90
DOWN = 270
MAX_HEIGHT = 260
MIN_HEIGHT = -260


class Paddle(Turtle):
    def __init__(self , xcor):
        super().__init__("square")
        self.penup()
        self.color("#D9CAB3")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(xcor, 0)

    def go_up(self):
        if self.ycor() < MAX_HEIGHT:
            new_y = self.ycor() + 20
            self.goto(self.xcor(), new_y)

    def go_down(self):
        if self.ycor() > MIN_HEIGHT:
            new_y = self.ycor() - 20
            self.goto(self.xcor(), new_y)
