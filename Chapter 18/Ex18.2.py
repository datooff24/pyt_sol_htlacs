import turtle

wn = turtle.Screen()
wn.bgcolor("lightgreen")

tess = turtle.Turtle()
tess.color("blue")


def cesaro(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        for angle in [-85, 170, -85, 0]:
            cesaro(t, order - 1, size / 2.175)
            t.left(angle)


def cesaro_square(t, order, size):
    for i in range(4):
        cesaro(t, order, size)
        t.right(90)

cesaro_square(tess, 1, 100)
cesaro_square(tess, 2, 100)
cesaro_square(tess,3,100)