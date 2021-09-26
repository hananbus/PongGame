from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("#77A8C6")
screen.title("Pong ")
screen.tracer(0)

right_paddle = Paddle(350)
left_paddle = Paddle(-350)

ball = Ball()

score_right = ScoreBoard(150)
score_left = ScoreBoard(-150)

screen.listen()
screen.onkey(right_paddle.go_up, "Up")
screen.onkey(right_paddle.go_down, "Down")
screen.onkey(left_paddle.go_up, "w")
screen.onkey(left_paddle.go_down, "s")
screen.onkey(left_paddle.go_up, "W")
screen.onkey(left_paddle.go_down, "S")

game_on = True
while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_with_wall()

    # collision with paddle
    if (ball.distance(right_paddle) < 50 and ball.xcor() > 320) or (
            ball.distance(left_paddle) < 50 and ball.xcor() < -320):
        ball.bounce_with_paddle()

    # someone score goal
    if ball.xcor() > 380:
        ball.goal()
        score_left.update_score()
    elif ball.xcor() < -380:
        ball.goal()
        score_right.update_score()

    # someone reach to 5 and win the game.
    # we update the score before the goal!
    if score_left.score == 6:
        score_left.game_over("left")
        game_on = False
    elif score_right.score == 6:
        score_right.game_over("right")
        game_on = False

screen.exitonclick()
