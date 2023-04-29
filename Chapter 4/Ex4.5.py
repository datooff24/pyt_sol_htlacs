import turtle


# angle 90 gives a square spiral, angle smaller than 90 gives a regular spiral


def draw_square_spiral(t, sz, ang):
    """Make turtle t draw a spiral with angle ang"""
    t.forward(sz)
    t.right(ang)
    t.forward(sz+1)
    t.right(ang)
    t.forward(sz+2)
    t.right(ang)
    t.forward(sz+3)
    t.right(ang)


wn = turtle.Screen()
wn.bgcolor("light green")
alex = turtle.Turtle()
alex.color("blue")
size = 1
angle = 89
for i in range(20):
    draw_square_spiral(alex, size, angle)
    size = size+4
wn.mainloop()
