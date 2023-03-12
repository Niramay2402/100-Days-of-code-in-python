from turtle import Turtle, Screen

timmy_the_turtle = Turtle()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("spring green")

for x in range(4):
    timmy_the_turtle.forward(100)
    timmy_the_turtle.left(90)


screen = Screen()
screen.exitonclick()