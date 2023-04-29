import turtle

# The """ """ comment is the docstring of the function. By printing print(function.__doc__) you can access the docstring


def draw_square(t, sz):
    """Make turtle t draw a square of size sz"""
    for i in range(4):
        t.forward(sz)
        t.left(90)


wn = turtle.Screen()
wn.bgcolor("light green")
wn.title("Alex meets a function")

alex = turtle.Turtle()
draw_square(alex, 50)
wn.mainloop()

# New script

def draw_multicolor_square(t, sz):
    """Make turtle t draw a multi-colored square of size sz"""
    for i in ["red", "purple", "hot pink", "blue"]:
        t.color(i)
        t.forward(sz)
        t.left(90)

wn = turtle.Screen()
wn.bgcolor("light green")

tess = turtle.Turtle()
tess.pensize(3)

size = 20
for i in range(15):
    draw_multicolor_square(tess, size)
    size = size+10
    tess.forward(10)
    tess.right(18)

wn.mainloop()
