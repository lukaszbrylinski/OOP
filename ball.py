from turtle import Turtle

class Ball (Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1
       # self.num_of_hits = 0

    def move_ball(self):
        new_x = self.xcor() + self.x_move #+ self.x_move * self.num_of_hits
        new_y = self.ycor() + self.y_move #+ self.y_move * self.num_of_hits
        self.goto(new_x, new_y)


    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9
       # self.num_of_hits += 1

    def reset_position(self):
        self.goto(0,0)
        self.bounce_x()
        self.move_speed = 0.1
        #self.num_of_hits = 0

