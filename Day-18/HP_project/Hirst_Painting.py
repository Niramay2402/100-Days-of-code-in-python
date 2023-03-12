# import colorgram
#
# rgb_colours = []
# colors = colorgram.extract('HirstD-Flumequine.jpg', 30)
#
# for color in colors:
#     r = color.rgb.r
#     b = color.rgb.b
#     g = color.rgb.g
#     C_tuple = (r, b, g)
#
#     rgb_colours.append(C_tuple)
#
# print(rgb_colours)
import random

color_list = [(243, 74, 225), (179, 29, 78), (49, 26, 36), (219, 76, 151), (146, 41, 28), (22, 69, 25), (44, 120, 43),
              (243, 239, 236), (170, 16, 21), (48, 158, 87), (210, 128, 85), (156, 86, 50), (120, 224, 160),
              (27, 28, 43), (215, 62, 79), (139, 140, 183), (115, 202, 106), (75, 57, 120), (65, 35, 30),
              (157, 231, 179), (150, 191, 211), (204, 43, 135), (86, 33, 87), (87, 109, 155), (202, 162, 121),
              (61, 170, 148), (55, 18, 100)]

# print(len(color_list))

import turtle as t
from turtle import Screen

tim = t.Turtle()
screen = Screen()
t.colormode(255)

screen.screensize(200, 100)
tim.speed(0)
tim.hideturtle()
tim.penup()
tim.setposition(-200, -200)
tim.setheading(0)

for y in range(5):
    for x in range(10):
        tim.dot(20, random.choice(color_list))
        tim.forward(50)

    tim.left(90)
    tim.forward(50)
    tim.left(90)

    for x in range(10):
        tim.forward(50)
        tim.dot(20, random.choice(color_list))

    tim.right(90)
    tim.forward(50)
    tim.right(90)

screen.exitonclick()
