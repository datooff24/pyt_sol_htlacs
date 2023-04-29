import turtle
wn = turtle.Screen()
wn.bgcolor("lightgreen")
color = ["red", "blue", "magenta"]
tess = turtle.Turtle()
tess.speed(100)
def sierpinski(t, order, size, changeColorDepth = -1):
    if order == 0:
        for angle in range(3): # basic case
            t.forward(size)
            t.left(120)

    else:
        if changeColorDepth == 0:
            t.color("red")
        sierpinski(t, order-1, size/2, changeColorDepth-1)
        if changeColorDepth == 0:
            t.color("blue")
        t.penup()
        t.forward(size/2)
        t.pendown()
        sierpinski(t, order-1, size/2, changeColorDepth-1)
        if changeColorDepth == 0:
            t.color("magenta")
        t.penup()
        t.back(size/2)
        t.left(60)
        t.forward(size/2)
        t.right(60)
        t.pendown()
        sierpinski(t, order-1, size/2, changeColorDepth-1)
        t.penup()
        t.right(120)
        t.forward(size/2)
        t.left(120)
sierpinski(tess, 5, 100, changeColorDepth=3)
wn.mainloop()