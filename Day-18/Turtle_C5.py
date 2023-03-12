# Make Spirograph
from turtle import Screen
import turtle as t
import random

tim = t.Turtle()
tim.speed(0)
t.colormode(255)


def random_colour():
    r = random.randint(0, 255)
    b = random.randint(0, 255)
    g = random.randint(0, 255)

    C_tuple = (r, b, g)
    return C_tuple


def draw_spirograph(size_of_gap):
    for x in range(int(360/size_of_gap)):
        tim.color(random_colour())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)


draw_spirograph(5)

screen = Screen()
screen.exitonclick()
