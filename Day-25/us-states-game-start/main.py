import turtle
import pandas

screen = turtle.Screen()
screen.title("United States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_state = []

while len(guessed_state) < 5:
    global guessed
    guessed = [*set(guessed_state)]
    answer_state = screen.textinput(title=f"{len(guessed)}/50 Guess The States", prompt="What's Another State?")

    if answer_state.title() == "Exit":
        missing_list = []
        for state in all_states:
            print(state)
            if state not in guessed:
                missing_list.append(state)
        print(missing_list)
        break

    if answer_state.title() in all_states:
        guessed_state.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state.title()]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(state_data.state.item())

# states to learn

print(guessed)

screen.exitonclick()







