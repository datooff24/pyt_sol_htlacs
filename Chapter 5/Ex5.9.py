import turtle


def draw_bar(t, height):
    """Get turtle t to draw one bar, of height."""
    if height >= 200:
         t.color("blue", "red")
    elif (height >= 100) and (height < 200):
        t.color("blue", "yellow")
    else:
        t.color("blue", "green")

    t.begin_fill()
    t.left(90)
    t.forward(height)
    if height < 0:
        t.penup()
        t.forward(-20)
        t.pendown()
        t.write("  " + str(height))
        t.penup()
        t.forward(20)
        t.pendown()
    else:
        t.write("  " + str(height))
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(height)
    t.left(90)
    t.end_fill()
    tess.penup()
    t.forward(10)
    tess.pendown()


wn = turtle.Screen()
wn.bgcolor("light green")

tess = turtle.Turtle()
tess.color("blue", "red")
tess.pensize(3)

xs = [48, 117, 200, 240, 160, 260, 220, -100]

tess.penup()
tess.forward(-200)
tess.pendown()
for a in xs:
    draw_bar(tess, a)
wn.mainloop()
