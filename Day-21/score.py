from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.goto(-10, 260)
        self.color('white')
        self.scores = 0
        self.update_score()

    def update_score(self):
        self.write(f"Score: {self.scores}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.penup()
        self.goto(0, 0)
        self.write("Game Over", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.scores += 1
        self.clear()
        self.update_score()
