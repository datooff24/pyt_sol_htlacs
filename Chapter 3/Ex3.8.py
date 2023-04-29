import turtle
data = [160, -43, 270, -97, -43, 200, -940, 17, -86]
wn = turtle.Screen()
pirate = turtle.Turtle()
total = 0
for angle in data:
    pirate.left(angle)
    pirate.forward(100)
    total = total+angle
wn.mainloop()
print("The drunk pirate's heading is", total%360, " degrees from zero counter-clockwise")
