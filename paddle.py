from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape('square')
        self.shapesize(1, 5, 15)
        self.color('white')
        self.penup()
        self.setheading(90)
        self.player_paddle(position)

    def player_paddle(self, pos):
        if pos == 'right':
            self.goto(350, 0)
        elif pos == 'left':
            self.goto(-350, 0)

    def up(self):
        self.forward(40)

    def down(self):
        self.backward(40)
