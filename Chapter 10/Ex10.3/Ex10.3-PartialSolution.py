# Partial solution to Ex10.3. 
# This code only includes one traffic light, not the one from Ex10.2 which the exercise asks us to include as well

import turtle           # Tess becomes a traffic light.

turtle.setup(400,500)
wn = turtle.Screen()
wn.title("Tess becomes a traffic light!")
wn.bgcolor("lightgreen")

green = turtle.Turtle()
orange = turtle.Turtle()
orange.hideturtle()
red = turtle.Turtle()
red.hideturtle()

def draw_housing():
    """ Draw a nice housing to hold the traffic lights """
    green.pensize(3)
    green.color("black", "darkgrey")
    green.begin_fill()
    green.forward(80)
    green.left(90)
    green.forward(200)
    green.circle(40, 180)
    green.forward(200)
    green.left(90)
    green.end_fill()


draw_housing()

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
orange.forward(40)
orange.left(90)
orange.forward(120)
orange.shape("circle")
orange.shapesize(3)
orange.fillcolor("orange")

# Same steps for the red light
red.penup()
red.forward(40)
red.left(90)
red.forward(190)
red.shape("circle")
red.shapesize(3)
red.fillcolor("red")

state_num = 0

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


advance_state_machine_alt()
wn.mainloop()
