import turtle


def draw_poly(t, n, sz):
    """Make turtle t draw a polygon with n sides of size sz"""
    for i in range(n):
        t.forward(sz)
        t.left(360/n)


wn = turtle.Screen()
wn.bgcolor("light green")
alex = turtle.Turtle()
alex.color("hot pink")
draw_poly(alex, 8, 50)
wn.mainloop()
