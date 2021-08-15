from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self, player):
        super().__init__()
        self.color('white')
        self.score = 0
        self.write(self.score, move=False, font=('Courier', 10, 'normal'))