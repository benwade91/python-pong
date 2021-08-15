from turtle import Screen
from paddle import Paddle

screen = Screen()
screen.setup(width=1000, height=800)
screen.bgcolor('black')
screen.title('Pong')

paddle = Paddle()


screen.exitonclick()