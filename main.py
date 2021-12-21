import turtle

import pandas

screen = turtle.Screen()
screen.title("U.S. State Game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

myTurtle = turtle.Turtle()

#def get_mouse_click_coor(x, y):
#    print(x, y)
#turtle.onscreenclick(get_mouse_click_coor)
#turtle.mainloop()
data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guesses = 0
myTurtle.penup()
previous_guesses = []
while guesses < 50:
    answer_state = screen.textinput(title=f"{guesses}/50 Guess the state", prompt="What's another state's name?")
    good_guess = data[(data.state).str.lower() == answer_state.lower()]
    newCity = good_guess["state"].str.cat(sep='\n')
    if answer_state.lower() == "exit":
        missing_states = ""
        for item in all_states:
            if item.lower() not in previous_guesses:
                missing_states += f"{item}\n"
        with open("states_to_learn.txt", mode='w+') as dw:
            dw.write(missing_states)
        break
#not a state's name or already considered
    if len(good_guess) != 0 and (newCity.lower() not in previous_guesses):
        myTurtle.goto(int(good_guess.x), int(good_guess.y))
        myTurtle .color("red")
        previous_guesses.append(newCity.lower())
        print(previous_guesses)
        myTurtle .write(newCity)
        print(good_guess["state"])
        guesses += 1


screen.exitonclick()