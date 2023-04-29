import turtle

alex = turtle.Turtle()
wn = turtle.Screen()

data = [(160, 20), (-43, 10), (270, 8), (-43, 12)]

for (angle, steps) in data:
    alex.left(angle)
    alex.forward(steps)
wn.mainloop()
