import turtle


def draw_star(t, sz):
    """make a turtle t draw a star with sides of size sz"""
    for i in range(5):
        t.forward(sz)
        t.right(144)


alex = turtle.Turtle()
alex.color("hot pink")
alex.pensize(3)
wn = turtle.Screen()
wn.bgcolor("light green")

# Moves the starting position to give the overal position a cleaner look
alex.penup()
alex.forward(-200)
alex.pendown()

for i in range(5):
    draw_star(alex, 100)
    alex.penup()
    alex.forward(350)
    alex.right(144)
    alex.pendown()
wn.mainloop()
