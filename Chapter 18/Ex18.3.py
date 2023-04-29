import turtle
wn = turtle.Screen()
wn.bgcolor("lightgreen")

tess = turtle.Turtle()
tess.speed(100)
def sierpinski(t, order, size):
    if order == 0:
        for angle in range(3): # basic case
            t.forward(size)
            t.left(120)
    else:
        sierpinski(t, order-1, size/2)
        t.penup()
        t.forward(size/2)
        t.pendown()
        sierpinski(t, order-1, size/2)
        t.penup()
        t.back(size/2)
        t.left(60)
        t.forward(size/2)
        t.right(60)
        t.pendown()
        sierpinski(t, order-1, size/2)
        t.penup()
        t.right(120)
        t.forward(size/2)
        t.left(120)
sierpinski(tess, int(input("What order do you want the Sierpinski triangle to be? ")), 100)
wn.mainloop()