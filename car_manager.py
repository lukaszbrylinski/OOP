import random
from turtle import Turtle
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.penup()
        self.color(random.choice(COLORS))
        self.goto(x=250, y=random.randint(-250, 250))

    def move_car(self, level):
        new_x = self.xcor() - STARTING_MOVE_DISTANCE - MOVE_INCREMENT * (level - 1)
        self.goto(x=new_x, y=self.ycor())

