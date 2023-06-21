import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. State Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
state_name = turtle.Turtle()
data = pandas.read_csv("50_states.csv")
state_list = data.state.to_list()

game_on = []

while len(game_on) < 50:
    if len(game_on) == 0:
        answer_state = turtle.textinput(title="Guess the State", prompt="What is a state name?")
    else:
        answer_state = turtle.textinput(title=f"{len(game_on)}/50 States", prompt="What is a state name?")

    if answer_state.title() == "Exit":
        missing_states = [state for state in state_list if state not in game_on]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("missing_states.csv")
        break

    coordinate = data[data.state == answer_state.title()]
    for state in state_list:
        if state == answer_state.title():
            state_name.penup()
            state_name.hideturtle()
            state_name.goto(int(coordinate.x), int(coordinate.y))
            state_name.write(state, align="center")
            game_on.append(answer_state.title())

