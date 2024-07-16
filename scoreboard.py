from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Courier', 16, 'normal')
with open("data.txt", mode="r") as file:
    HIGHSCORE = int(file.read())

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = HIGHSCORE
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.upgrade_scoreboard()

    def upgrade_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.color("white")
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)
        print(f'score{self.score}')

    def reset_game(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as data:
                data.write(str(self.score))
        self.score = 0
        self.upgrade_scoreboard()
