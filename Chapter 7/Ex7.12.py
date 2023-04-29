import turtle
import math

alex = turtle.Turtle()
wn = turtle.Screen()

house_data = [(0, 100), (90, 100), (90, 100), (90, 100), (135, math.sqrt(20000)), (90, math.sqrt(5000)),
              (90, math.sqrt(5000)), (90, math.sqrt(20000))]

for (angle, steps) in house_data:
    alex.left(angle)
    alex.forward(steps)
wn.mainloop()
