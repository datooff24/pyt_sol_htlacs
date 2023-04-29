import turtle


def draw_star(t, sz):
    """make a turtle t draw a star with sides of size sz"""
    for i in range(5):
        t.forward(sz)
        t.right(144)


alex = turtle.Turtle()
wn = turtle.Screen()
draw_star(alex, 100)
wn.mainloop()
