# Importing the required modules
import turtle
import pandas

# Creating the screen for displaying the map
screen = turtle.Screen()
screen.title('U.S. States Game')
image = 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)

# Get the list of all the states
data = pandas.read_csv('50_states.csv')
state_list = data.state.to_list()

# Empty list to keep track of all the guessed states
guessed_states = []

# While loop to keep guessing
while len(guessed_states) < 50:
    answer = screen.textinput(title=f'{len(guessed_states)}/50 Guess the State',
                              prompt='What is another state name :').title()

    # Condition to stop guessing
    if answer == 'Exit':
        missing_state = [state for state in state_list if state not in guessed_states]
        new_data = pandas.DataFrame(missing_state)
        new_data.to_csv('missing_states.csv')  # To keep a list of all the un-guessed states
        break

    # Condition if guessed state is correct and adding in our guessed state list
    if answer in state_list:
        tim = turtle.Turtle()
        tim.hideturtle()
        tim.penup()
        state_data = data[data.state == answer]
        x_cor = int(state_data.x)
        y_cor = int(state_data.y)
        tim.goto(x_cor, y_cor)
        tim.write(f'{answer}', font=('Arial', 10, 'normal'))
        guessed_states.append(answer)
