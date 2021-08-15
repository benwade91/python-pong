from turtle import Turtle

BALL_SPEED = 0.5

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.penup()
        self.x_direction = BALL_SPEED
        self.y_direction = BALL_SPEED

    def move(self):
        new_x = self.xcor() + self.x_direction
        new_y = self.ycor() + self.y_direction
        self.goto(new_x, new_y)

    def bounce(self, what_bounced):
        if what_bounced == 'wall':
            self.y_direction *= -1
        elif what_bounced == 'paddle':
            self.x_direction *= -1
