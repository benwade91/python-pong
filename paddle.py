from turtle import Turtle

class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('square')
        self.shapesize(1, 5, 15)
        self.color('white')
        self.penup()
        self.setheading(90)

    def player_paddle(self, pos):
        if pos == 'right':
            self.goto(400, 0)
        elif pos == 'left':
            self.goto(-400, 0)

    def up(self):
        self.forward(20)

    def down(self):
        self.backward(20)
