from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.level = 1
        self.goto(-200, 250)
        # self.write(f"Level {self.level}", align="center", font=FONT)

    def update_level(self):
        self.clear()
        self.level += 1
        self.write(f"Level {self.level}", align="center", font=FONT)



