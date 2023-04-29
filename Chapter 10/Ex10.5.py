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
green.fillcolor("grey")

# Same steps for the orange light
orange.penup()
orange.forward(40)
orange.left(90)
orange.forward(120)
orange.shape("circle")
orange.shapesize(3)
orange.fillcolor("grey")
orange.showturtle()

# Same steps for the red light
red.penup()
red.forward(40)
red.left(90)
red.forward(190)
red.shape("circle")
red.shapesize(3)
red.fillcolor("grey")
red.showturtle()


state_num = 0  # start at red, so it will jump to green immediately?

# Same idea as Ex10.3, but instead of hiding the lights, we make them grey
def advance_state_machine_alt():
    global state_num
    if state_num == 0:
        red.color("grey")
        orange.color("grey")
        green.color("green")
        state_num = 1
        wn.ontimer(advance_state_machine_alt, 3000)
    elif state_num == 1:
        green.color("green")
        orange.color("orange")
        red.color("grey")
        state_num = 2
        wn.ontimer(advance_state_machine_alt, 1000)
    elif state_num == 2:
        red.color("grey")
        orange.color("orange")
        green.color("grey")
        state_num = 3
        wn.ontimer(advance_state_machine_alt, 1000)
    elif state_num == 3:
        red.color("red")
        orange.color("grey")
        green.color("grey")
        state_num = 0
        wn.ontimer(advance_state_machine_alt, 2000)


advance_state_machine_alt()
wn.mainloop()
