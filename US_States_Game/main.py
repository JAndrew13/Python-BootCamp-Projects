#get states positions tool
# def get_mouse_click_coor(x,y):
#     print(x,y)
# turtle.onscreenclick(get_mouse_click_coor)

#~~~~ INIT GAME ~~~~#

#initiate screen/game
import turtle
screen = turtle.Screen()
screen.title("U.S. States Game")

#load blackground image
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


#~~~~ DATA ~~~~#

#import pandas and state csv
import pandas
data = pandas.read_csv("50_states.csv")

#create list of states in lowercase
state_names = []
for i in data["state"]:
    name = i
    state_names.append(name)
print(state_names)

CORRECT_ANSWERS = []

#display name

def display(answer_state):
    t = turtle.Turtle()
    t.hideturtle()
    t.penup()
    state_data = data[data.state == answer_state]
    xcor = int(state_data["x"])
    ycor = int(state_data["y"])
    t.goto(xcor, ycor)
    t.write(answer_state, align="center", font=("Ariel", 6, 'bold'))


#record answer in list

def record(answer_state):
    CORRECT_ANSWERS.append(answer_state)
    print(f"Correct Answers: {len(CORRECT_ANSWERS)}'/50'")




while len(CORRECT_ANSWERS) < 50:
#Create Type Prompt for answers
    answer_state = screen.textinput(title="Guess the State", prompt="What's another state's name?")
    print(answer_state)

    #check if answer is good or bad
    if not answer_state.title() in state_names:
        print("Incorrect, check spelling and guess again!")
    elif answer_state in CORRECT_ANSWERS:
        print("You already guessed that!")
    else:
        print("You are correct!")
        record(answer_state)
        display(answer_state.title())

#Game Complete!
print("You guessed all the states! Congradulations")

#GAME START
# state_data = data[data.state == "Texas"]
# print(int(state_data["x"]))




# for i in state_data["state"]:

# if not answer_state.lower() in state_data["state"].lower():
#     print("state not found")
# else: print("correct!")