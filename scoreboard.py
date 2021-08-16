from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self, player):
        super().__init__()
        self.color('white')
        self.penup()
        self.score = 0
        self.player_score(player)
        self.write(self.score, move=False, font=('Courier', 50, 'bold'))
        self.hideturtle()

    def player_score(self, pos):
        if pos == 'left':
            self.goto(-100, 250)
        elif pos == 'right':
            self.goto(100, 250)

    def add_point(self):
        self.clear()
        self.score += 1
        self.write(self.score, move=False, font=('Courier', 50, 'bold'))
        print(self.score)