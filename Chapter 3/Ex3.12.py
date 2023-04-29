import turtle
wn = turtle.Screen()
wn.bgcolor("light green")
alex = turtle.Turtle()
alex.shape("turtle")
alex.color("blue")
alex.stamp()
for i in range(12):
    alex.penup()
    alex.forward(200)
    alex.stamp()
    alex.forward(-200)
    alex.left(30)
wn.mainloop()
