import turtle


def draw_poly(t, n, sz):
    """Make turtle t draw a polygon with n sides of size sz"""

    for i in range(n):
        t.forward(sz)
        t.left(360 / n)


def draw_equitriangle(t, sz):
    """Make turtle t draw an equilateral triangle of size sz"""
    draw_poly(t, 3, sz)


wn = turtle.Screen()
wn.bgcolor("light green")
alex = turtle.Turtle()
alex.color("hot pink")
draw_equitriangle(alex, 100)
wn.mainloop()
