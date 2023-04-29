import turtle
data = [160, -43, 270, -97, -43, 200, -940, 17, -86]
wn = turtle.Screen()
pirate = turtle.Turtle()
for angle in data:
    pirate.left(angle)
    pirate.forward(100)
wn.mainloop()

