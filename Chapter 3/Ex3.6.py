import turtle
wn = turtle.Screen()
alex = turtle.Turtle()
alex.shape("turtle")
# Equilateral triangle
for i in range(3):
    alex.forward(100)
    alex.left(120)
# Square
for i in range(4):
    alex.forward(100)
    alex.left(90)
# Hexagon
for i in range(6):
    alex.forward(100)
    alex.left(60)
# Octagon
for i in range(8):
    alex.forward(100)
    alex.left(45)
wn.mainloop()