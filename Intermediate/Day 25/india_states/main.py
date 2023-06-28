import pandas
import turtle

t = turtle.Turtle()
t.hideturtle()
t.penup()


def plot_state_on_screen(state_name):
    state_data = data[data.state == state_name]
    t.goto(int(state_data.x), int(state_data.y))
    t.write(answer_state)


screen = turtle.Screen()
screen.title("India States Game")
image = "india_blank_states.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("india_states.csv")


all_states = data["state"].to_list()
guessed_states = []


while len(guessed_states) < 28:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/28 States Correct",
                                    prompt="What's another state's name?").title()

    if answer_state in all_states:
        # Show State on Map
        plot_state_on_screen(answer_state)
        guessed_states.append(answer_state)

    if answer_state == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
