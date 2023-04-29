import turtle


class TurtleGTX(turtle.Turtle):

    # Add odometer as an attribute to TurtleGTX
    def __init__(self, odometer=0):
        super().__init__()
        self.odometer = odometer

    def jump(self, distance):
        self.penup()
        self.forward(distance)
        self.pendown()

    # Edit the forward method to include the odometer
    # Log each unit distance traveled into cromometer.
    # This will slow the program down, but it is required for Ex 23.3
    def forward(self, distance):
        for step in range(abs(distance)):
            if distance >= 0:
                self.odometer += 1
                self.fd(1)
            else:
                self.odometer += 1
                self.fd(-1)
        print("The traveled distance is " + str(self.odometer))


tess = TurtleGTX()
wn = tess.getscreen()
tess.forward(-50)
tess.forward(150)
wn.mainloop()
