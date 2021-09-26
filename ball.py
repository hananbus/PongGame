from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__("circle")
        self.color("#986D8E")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_with_wall(self):
        self.y_move *= -1

    def bounce_with_paddle(self):
        self.x_move *= -1
        self.move_speed *= 0.8

    def goal(self):
        self.move_speed = 0.1
        self.x_move *= -1
        self.goto(0, 0)



