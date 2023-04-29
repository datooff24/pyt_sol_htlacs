import turtle


def draw_square(t, sz):
    """Make turtle t draw a square of size sz"""
    for i in range(4):
        t.forward(sz)
        t.left(90)
    t.penup()
    t.forward(2*sz)
    t.pendown()


wn = turtle.Screen()
wn.bgcolor("light green")
alex = turtle.Turtle()
alex.color("hot pink")


for i in range(4):
    draw_square(alex, 20)

wn.mainloop()
