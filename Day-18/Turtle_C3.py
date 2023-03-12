from turtle import Turtle, Screen
import random

timmy_the_turtle = Turtle()
timmy_the_turtle.shape("turtle")
colours = ["dark cyan", "teal", "dark slate gray", "steel blue", "deep pink", "pale green", "CornflowerBlue",
           "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

sides = 3
timmy_the_turtle.speed(0)

for x in range(5):
    timmy_the_turtle.color(random.choice(colours))
    for y in range(sides):
        angle = 360 / sides
        timmy_the_turtle.forward(100)
        timmy_the_turtle.right(angle)
    sides += 1

screen = Screen()
screen.exitonclick()
