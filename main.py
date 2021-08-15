from turtle import Screen
from paddle import Paddle

screen = Screen()
screen.setup(width=1000, height=800)
screen.bgcolor('black')
screen.title('Pong')
screen.tracer(0)

right_player = Paddle()
right_player.player_paddle('right')
left_player = Paddle()
left_player.player_paddle('left')

screen.listen()
screen.onkey(right_player.up, 'Up')
screen.onkey(right_player.down, 'Down')
screen.onkey(left_player.up, 'a')
screen.onkey(left_player.down, 'z')

game_on = True

while game_on:
    screen.update()



screen.exitonclick()