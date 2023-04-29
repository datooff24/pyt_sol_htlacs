class Point:
    """Point class represents and manipulates x,y coords. """

    def __init__(self, x=0, y=0):
        """Create a new point at the origin"""
        self.x = x
        self.y = y

    def __str__(self):
        return "({0}, {1})".format(self.x, self.y)

    def halfway(self, target):
        """ Return the halfway point between myself and the target """
        mx = (self.x + target.x) / 2
        my = (self.y + target.y) / 2
        return Point(mx, my)

    # Ex 15.2
    def reflection_x_axis(self):
        """Reflects a point around the x-axis"""
        return Point(self.x, -self.y)

    # Ex 15.3
    def slope_from_origin(self):
        """Returns the slope of the line joining the origin to the point"""
        return self.y / self.x

    # Ex 15.4
    def get_line_to(self, secondpoint):
        """computes the coefficients a, b in y = ax+b"""
        a = (secondpoint.y - self.y) / (secondpoint.x - self.x)
        b = self.y - a * self.x
        return (a, b)


# Ex 15.5

# Does not work if the two bisector lines completely overlap
# This occurs if both slopes of the lines connecting the points are the same

def midpoint_circle(p1, p2, p3, p4):
    # compute the slopes of p1,p2 and p3,p4
    line1 = p1.get_line_to(p2)
    slope1 = line1[0]
    line2 = p3.get_line_to(p4)
    slope2 = line2[0]

    # compute two midpoints:
    midpoint1 = p1.halfway(p2)
    midpoint2 = p3.halfway(p4)

    # compute bisectors y=ax+b for line1 and line2, starting at midpoint1 and midpoint2 respectively
    bisector1_slope = -1 / slope1
    bisector2_slope = -1 / slope2

    bisector1_b = midpoint1.y - bisector1_slope * midpoint1.x
    bisector2_b = midpoint2.y - bisector2_slope * midpoint2.x

    # initial value is the midpoint of one of the coordinates, this assures we're not too far away from the center
    # make epsilon smaller to get more accurate results
    # note that the incremental changes in x will need to be smaller than epsilon to avoid infinite loop
    x = midpoint1.x
    epsilon = 0.01

    # compute y-distance for fixed x
    # increase x to see if larger x gets us closer to the midpoint i.e. decreases the distance
    distance_old = abs((bisector1_slope - bisector2_slope) * x + (bisector1_b - bisector2_b))
    x += 0.005
    distance_new = abs((bisector1_slope - bisector2_slope) * x + (bisector1_b - bisector2_b))

    # Two cases: either the distances are decreasing or increasing
    # Depending on this we keep increasing or decreasing the x values until we reach the midpoint of the circle

    if distance_new < distance_old:
        while True:
            if distance_new <= epsilon:
                return x, bisector1_slope * x + bisector1_b
            x += 0.005
            distance_new = abs((bisector1_slope - bisector2_slope) * x + (bisector1_b - bisector2_b))
    elif distance_new > distance_old:
        while True:
            if distance_new <= epsilon:
                return x, bisector1_slope * x + bisector1_b
            x -= 0.005
            distance_new = abs((bisector1_slope - bisector2_slope) * x + (bisector1_b - bisector2_b))
    else:
        return "The function will not work with these chosen points. Pick different points."


import math

# As an example we take points on the unit circle, whose center is (0,0)
p1 = Point(0.5, 0.5 * math.sqrt(3))
p2 = Point(0, 1)
p3 = Point(-1, 0)
p4 = Point(0, -1)

print("The coordinates of the midpoint of this circle are", midpoint_circle(p1, p2, p3, p4))
