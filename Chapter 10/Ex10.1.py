import turtle

turtle.setup(400,500)                # Determine the window size
wn = turtle.Screen()                 # Get a reference to the window
wn.title("Handling keypresses!")     # Change the window title
wn.bgcolor("lightgreen")             # Set the background color
tess = turtle.Turtle()               # Create our favorite turtle

# The next four functions are our "event handlers".
def h1():
   tess.forward(30)

def h2():
   tess.left(45)

def h3():
   tess.right(45)

def h4():
    wn.bye()                        # Close down the turtle window

# Press buttons to change colors

def red():
    tess.color("red")

def green():
    tess.color("green")

def blue():
    tess.color("blue")

# Press + or - to change size

default_pensize = 1

def larger():
    global default_pensize
    if default_pensize < 20:
        tess.pensize(default_pensize+1)
    else:
        tess.pensize(20)

def smaller():
    global default_pensize
    if default_pensize > 1:
        tess.pensize(default_pensize - 1)
    else:
        tess.pensize(0)

# 1, 2 or 3 changes the shape of tess into a default, turtle or circle respectively

def tess_to_default():
    tess.shape("classic")

def tess_to_turtle():
    tess.shape("turtle")

def tess_to_circle():
    tess.shape("circle")


# These lines "wire up" keypresses to the handlers we've defined.
wn.onkey(h1, "Up")
wn.onkey(h2, "Left")
wn.onkey(h3, "Right")
wn.onkey(h4, "q")

wn.onkey(red, "r")
wn.onkey(blue, "b")
wn.onkey(green, "g")

wn.onkey(larger, "+")
wn.onkey(smaller, "-")

wn.onkey(tess_to_default, "1")
wn.onkey(tess_to_turtle, "2")
wn.onkey(tess_to_circle, "3")

# Now we need to tell the window to start listening for events,
# If any of the keys that we're monitoring is pressed, its
# handler will be called.
wn.listen()
wn.mainloop()
