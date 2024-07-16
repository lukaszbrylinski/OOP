from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.hideturtle()
        self.color("black")
        self.update_scoreboard()


    def update_scoreboard(self):
        self.clear()
        self.goto(-200, 200)
        self.write(f"Level: {self.level}", align="center",font=FONT)

    def level_up(self):
        self.level += 1
        self.update_scoreboard()