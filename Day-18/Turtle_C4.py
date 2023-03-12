# Random Walk
from turtle import Turtle, Screen
import random

timmy_the_turtle = Turtle()
timmy_the_turtle.shape("turtle")
colours = ["dark cyan", "teal", "dark slate gray", "steel blue", "deep pink", "pale green", "CornflowerBlue",
           "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

# using rgb color for randomising colour
# t.colormode(255)
#
#
# def random_colour():
#     r = random.randint(0, 255)
#     b = random.randint(0, 255)
#     g = random.randint(0, 255)
#     C_tuple = (r, b, g)
#
#     return C_tuple

directions = [0, 90, 180, 270]
timmy_the_turtle.pensize(10)
timmy_the_turtle.speed(0)

for x in range(200):
    timmy_the_turtle.forward(30)
    timmy_the_turtle.setheading(random.choice(directions))
    timmy_the_turtle.color(random.choice(colours))

screen = Screen()
screen.exitonclick()