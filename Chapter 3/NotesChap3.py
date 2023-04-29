# import the turtle module
import turtle

# wn is the Screen type that is defined within turtle
# alex is the Turtle type that is defined within turtle
wn = turtle.Screen()
wn.bgcolor("lightgreen")
wn.title("Hello, Alex!")
alex = turtle.Turtle()
alex.shape("turtle")

alex.penup()
size = 20
for i in range(30):
    alex.stamp()
    size = size+3
    alex.forward(size)
    alex.right(size)
wn.mainloop()
