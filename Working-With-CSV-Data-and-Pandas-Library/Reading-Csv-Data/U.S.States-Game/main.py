import turtle
import  pandas
screen=turtle.Screen()
screen.title('U.S. States Game')
image='blank_states_img.gif'

screen.addshape(image)
turtle.shape(image)
data=pandas.read_csv('50_states.csv')
all_states=data['state'].to_list()
guessed_states=[]

while len(guessed_states)<50:
    answer_state=screen.textinput(title='{}/50 the State Correct'.format(len(guessed_states)),
                                  prompt="What's another state's name?").title()
    if answer_state=='Exit':
        missing_state=[]
        for state in all_states:
            if state not in guessed_states:
                missing_state.append(state)
        new_data=pandas.DataFrame(missing_state)
        new_data.to_csv('states_to_learn.csv')
        break
    if answer_state in all_states:
        guessed_states.append(answer_state)
        t=turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data=data[data.state==answer_state]
        t.goto(int(state_data['x']),int(state_data['y']))
        t.write(answer_state)
    answer_state
screen.exitonclick()
