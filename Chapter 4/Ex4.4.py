import turtle


def draw_square(t, sz):
    """Make turtle t draw a square of size sz"""
    for i in range(4):
        t.forward(sz)
        t.left(90)


wn = turtle.Screen()
wn.bgcolor("light green")
alex = turtle.Turtle()
alex.color("blue")
for i in range(20):
    draw_square(alex, 50)
    alex.left(18)
alex.penup()
wn.mainloop()
