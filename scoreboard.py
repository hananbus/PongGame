from turtle import Turtle

FONT = ("Courier", 24, "normal")


class ScoreBoard(Turtle):
    def __init__(self, x_pos):
        super().__init__()
        self.hideturtle()
        self.color("#D9CAB3")
        self.goto(x_pos, 260)
        self.score = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score}", align='center', font=FONT)
        self.score += 1

    def game_over(self, who_won):
        self.goto(0,0)
        self.write(f"Game Over, {who_won} player win!", align='center', font=FONT)
