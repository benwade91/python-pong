from turtle import Turtle

class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('square')
        self.shapesize(5, 1, 15)
        self.color('white')
        self.penup()

    def player_paddle(self, pos):
        if pos == 'right':
            self.goto(350, 0)
        elif pos == 'left':
            self.goto(-350, 0)