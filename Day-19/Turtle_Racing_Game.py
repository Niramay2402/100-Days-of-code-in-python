from turtle import Turtle, Screen
import random

screen = Screen()
is_race_on = False
screen.setup(500, 400)
user_input = screen.textinput(title="Make Your Bet", prompt="Who from the TMN turtles would win.? Enter From [R M L D]:")
# print(user_input)

Leo = Turtle(shape="turtle")
Leo.color("blue")
Leo.penup()

Mickey = Turtle(shape="turtle")
Mickey.color("orange")
Mickey.penup()

Ralph = Turtle(shape="turtle")
Ralph.color("red")
Ralph.penup()

Donnie = Turtle(shape="turtle")
Donnie.color("purple")
Donnie.penup()

Leo.goto(x=-250, y=100)
Ralph.goto(x=-250, y=50)
Mickey.goto(x=-250, y=0)
Donnie.goto(x=-250, y=-50)

all_turtles = [Leo, Ralph, Mickey, Donnie]

if user_input:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 230:
            winner = turtle.pencolor()
            is_race_on = False
        rand_dist = random.randint(1, 10)
        turtle.forward(rand_dist)


if user_input == winner:
    print("Your prediction was Correct\n")
    print("You Won")
else:
    print("Your prediction was Wrong")


screen.exitonclick()
