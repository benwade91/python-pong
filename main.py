from turtle import Screen
from paddle import Paddle
from ball import Ball

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title('Pong')
screen.tracer(0)

right_player = Paddle('right')
left_player = Paddle('left')
ball = Ball()

screen.listen()
screen.onkey(right_player.up, 'Up')
screen.onkey(right_player.down, 'Down')
screen.onkey(left_player.up, 'a')
screen.onkey(left_player.down, 'z')

game_on = True

while game_on:
    screen.update()
    ball.move()

    # handle wall bounce
    if ball.ycor() > 30 or ball.ycor() < -30:
        ball.bounce('wall')

    # handle paddle bounce
    #     right paddle
    if ball.distance(right_player) < 50 and ball.xcor() > 325:
        ball.bounce('paddle')
    #     left paddle
    if ball.distance(left_player) < 50 and ball.xcor() < -325:
        ball.bounce('paddle')


screen.exitonclick()