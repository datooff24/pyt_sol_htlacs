import turtle

screen_color = input("What color do you want the background to be? ")
turtle_color = input("What color do you want the turtle to be? ")
pen_size = input("What pensize do you want? ")
wn = turtle.Screen()
wn.bgcolor(screen_color)
wn.title("Hello, Alex!")
alex = turtle.Turtle()
alex.color(turtle_color)
alex.pensize(int(pen_size))

alex.forward(50)
alex.left(120)
alex.forward(30)


wn.mainloop()
