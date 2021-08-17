from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.penup()
        self.ball_speed = 0.5
        self.x_direction = self.ball_speed
        self.y_direction = self.ball_speed

    def move(self):
        new_x = self.xcor() + self.x_direction
        new_y = self.ycor() + self.y_direction
        self.goto(new_x, new_y)

    def bounce(self, what_bounced):
        if what_bounced == 'wall':
            self.y_direction *= -1
        elif what_bounced == 'paddle':
            self.x_direction *= -1.1
