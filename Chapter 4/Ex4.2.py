import turtle


def draw_square_2(t, sz):
    """Make turtle t draw a square of size sz"""
    for i in range(4):
        t.forward(sz)
        t.left(90)
    t.penup()
    t.forward(-10)
    t.right(90)
    t.forward(10)
    t.left(90)
    t.pendown()


wn = turtle.Screen()
wn.bgcolor("light green")
alex = turtle.Turtle()
alex.color("hot pink")

size = 20

for i in range(5):
    draw_square_2(alex, size)
    size = size+20
wn.mainloop()

