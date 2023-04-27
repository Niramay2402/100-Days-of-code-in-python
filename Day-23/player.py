from turtle import Turtle
from car_manager import CarManager
from scoreboard import Scoreboard

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

level = Scoreboard()
Car = CarManager()


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")

        self.color("green")
        self.penup()
        self.goto(STARTING_POSITION)
        self.left(90)

    def go_up(self):
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(), new_y)

    def lvl_update(self):
        level.increase_lvl()
        Car.car_speed += 10
        self.goto(STARTING_POSITION)


class FinishLine(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.color("black")
        self.goto(-300, 240)

    def draw_fl(self):
        for i in range(30):
            self.pendown()
            self.forward(10)
            self.penup()
            self.forward(10)





