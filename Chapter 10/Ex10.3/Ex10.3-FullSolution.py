# Full solution to exercise 10.3, which asks us to create two different traffic lights next to one another

import turtle           # Tess becomes a traffic light.

turtle.setup(800,500)
wn = turtle.Screen()
wn.title("Tess becomes a traffic light!")
wn.bgcolor("lightgreen")

tess = turtle.Turtle()
green = turtle.Turtle()
orange = turtle.Turtle()
orange.hideturtle()
red = turtle.Turtle()
red.hideturtle()

def draw_housing():
    """ Draw a nice housing to hold the traffic lights """
    tess.pensize(3)
    tess.color("black", "darkgrey")
    tess.begin_fill()
    tess.forward(80)
    tess.left(90)
    tess.forward(200)
    tess.circle(40, 180)
    tess.forward(200)
    tess.left(90)
    tess.end_fill()

    # Create a second traffic light next to the first one
    green.pensize(3)
    green.color("black", "darkgrey")

    # Move the second traffic light to the right
    green.penup()
    green.forward(200)
    green.pendown()

    green.begin_fill()
    green.forward(80)
    green.left(90)
    green.forward(200)
    green.circle(40, 180)
    green.forward(200)
    green.left(90)
    green.end_fill()


draw_housing()
tess.penup()
# Position tess onto the place where the green light should be
tess.forward(40)
tess.left(90)
tess.forward(50)
# Turn tess into a big green circle
tess.shape("circle")
tess.shapesize(3)
tess.fillcolor("green")

green.penup()
# Position green onto the place where the green light should be
green.forward(40)
green.left(90)
green.forward(50)
# Turn green into a big green circle
green.shape("circle")
green.shapesize(3)
green.fillcolor("green")

# Same steps for the orange light
orange.penup()
orange.forward(200) # Move orange to the second light
orange.forward(40)
orange.left(90)
orange.forward(120)
orange.shape("circle")
orange.shapesize(3)
orange.fillcolor("orange")

# Same steps for the red light
red.penup()
red.forward(200) # Move red to the second light
red.forward(40)
red.left(90)
red.forward(190)
red.shape("circle")
red.shapesize(3)
red.fillcolor("red")

state_num = 0
state_num_tess = 0

def advance_state_machine_alt():
    global state_num
    if state_num == 0:
        green.showturtle()
        red.hideturtle()
        orange.hideturtle()
        state_num = 1
    elif state_num == 1:
        green.hideturtle()
        orange.showturtle()
        red.hideturtle()
        state_num = 2
    else:
        red.showturtle()
        orange.hideturtle()
        green.hideturtle()
        state_num = 0
    wn.ontimer(advance_state_machine_alt, 2000)

def advance_state_machine():
    global state_num_tess
    if state_num_tess == 0:
        # Transition from state 0 to state 1
        tess.forward(70)
        tess.fillcolor("orange")
        state_num_tess = 1
    elif state_num_tess == 1:     # Transition from state 1 to state 2
        tess.forward(70)
        tess.fillcolor("red")
        state_num_tess = 2
    else:                    # Transition from state 2 to state 0
        tess.back(140)
        tess.fillcolor("green")
        state_num_tess = 0
    wn.ontimer(advance_state_machine, 2000)


advance_state_machine_alt()
advance_state_machine()
wn.mainloop()
