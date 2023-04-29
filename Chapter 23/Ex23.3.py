import turtle


class TurtleGTX(turtle.Turtle):
    # Add odometer and maximum distance as attributes to TurtleGTX
    # Add attribute tire_distance, which measures the distance Turtle moves on a tire, in order to implement change_tire
    def __init__(self, tire_distance=0, max_dist=100, odometer=0):
        super().__init__()
        self.max_dist = max_dist
        self.odometer = odometer
        self.tire_distance = tire_distance

    def jump(self, distance):
        self.penup()
        self.fd(distance)
        self.pendown()

    # Edit the forward method to include the odometer
    def forward(self, distance):

        # Prevent forward from being called
        if self.tire_distance == self.max_dist:
            print("Turtle has a flat tire, and so cannot move forward")
            return None

        for step in range(abs(distance)):
            # if the tire distance has not reached the maximum distance, keep going
            # otherwise, stop the turtle from moving
            if self.tire_distance < self.max_dist:
                if distance >= 0:
                    self.odometer += 1
                    self.tire_distance += 1
                    self.fd(1)
                else:
                    self.odometer += 1
                    self.tire_distance += 1
                    self.fd(-1)
            else:
                print("The traveled distance is " + str(self.odometer) + ". Oh no! Turtle has a flat tire!")
                return None
        print("The traveled distance is " + str(self.odometer))

    def change_tire(self):
        self.tire_distance = 0
        print("The tire has been fixed!")


# Test
tess = TurtleGTX()
wn = tess.getscreen()

tess.jump(50)
tess.forward(50)
tess.forward(-60)
tess.change_tire()
tess.forward(60)
tess.forward(80)
tess.forward(40)

wn.mainloop()
