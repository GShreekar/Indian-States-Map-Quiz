import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("Indian States Game")
name = "India.gif"
screen.addshape(name)
turtle.shape(name)

data = pd.read_csv("all_states.csv")
all_states = data.State.to_list()
guessed_states = []

while len(guessed_states) < 32:

    answer_state = screen.textinput(title=f"{len(guessed_states)}/31 States Guessed.", prompt="What's another state's name?").title()

    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.State == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(state_data.State.item())

screen.mainloop()