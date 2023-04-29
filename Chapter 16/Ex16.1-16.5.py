import copy
from Chap16Tests import test
class Point:
    """Point class represents and manipulates x,y coords. """

    def __init__(self, x=0, y=0):
        """Create a new point at the origin"""
        self.x = x
        self.y = y

    def __str__(self):
        return "({0}, {1})".format(self.x, self.y)

class Rectangle:
    """ A class to manufacture rectangle objects """

    def __init__(self, posn, w, h):
        """ Initialize rectangle at posn, with width w, height h """
        self.corner = posn
        self.width = w
        self.height = h

    def __str__(self):
        return  "({0}, {1}, {2})".format(self.corner, self.width, self.height)

    # Ex 16.1
    def area(self):
        """returns the area of a rectangle"""
        area = self.width * self.height
        return area

    # Ex 16.2
    def perimeter(self):
        """returns the perimeter of a rectangle"""
        perimeter = 2 * self.width + 2 * self.height
        return perimeter

    # Ex 16.3
    def flip(self):
        """flips the width and height of a rectangle"""
        new_height = copy.copy(self.width)
        new_width = copy.copy(self.height)
        self.width = new_width
        self.height = new_height

    # Ex 16.4
    def contains(self, p):
        """tests if a Point p falls within a rectangle"""
        # First check if the point lies within the x-range of the rectangle
        if self.corner.x <= p.x < self.corner.x + self.width:
            # Secondly check if the point lies within the y-range of the rectangle
            if self.corner.y <= p.y < self.corner.y + self.height:
                return True
            else:
                return False
        else:
            return False

r = Rectangle(Point(0, 0), 10, 5)
test(r.area() == 50)

r = Rectangle(Point(0, 0), 10, 5)
test(r.perimeter() == 30)

r = Rectangle(Point(100, 50), 10, 5)
test(r.width == 10 and r.height == 5)
r.flip()
test(r.width == 5 and r.height == 10)

r = Rectangle(Point(0, 0), 10, 5)
test(r.contains(Point(0, 0)))
test(r.contains(Point(3, 3)))
test(not r.contains(Point(3, 7)))
test(not r.contains(Point(3, 5)))
test(r.contains(Point(3, 4.99999)))
test(not r.contains(Point(-3, -3)))


# Ex 16.5

def rect_clash(rect1, rect2):
    """tests if two rectangles collide"""
    # Compute all the corners of both rectangles and save the corners in a list.
    # Original rectangle:
    x_rect1 = Point()
    x_rect1.x = rect1.corner.x + rect1.width
    x_rect1.y = rect1.corner.y

    y_rect1 = Point()
    y_rect1.x = rect1.corner.x
    y_rect1.y = rect1.corner.y + rect1.height

    xy_rect1 = Point()
    xy_rect1.x = x_rect1.x
    xy_rect1.y = y_rect1.y

    rect1corners = [rect1.corner, x_rect1, y_rect1, xy_rect1]

    # Second rectangle:
    x_rect2 = Point()
    x_rect2.x = rect2.corner.x + rect2.width
    x_rect2.y = rect2.corner.y

    y_rect2 = Point()
    y_rect2.x = rect2.corner.x
    y_rect2.y = rect2.corner.y + rect2.height

    xy_rect2 = Point()
    xy_rect2.x = x_rect1.x
    xy_rect2.y = y_rect1.y

    rect2corners = [rect2.corner, x_rect2, y_rect2, xy_rect2]

    # Case 1: corner of rect1 inside rect2:
    for corner in rect1corners:
        if rect2.contains(corner):
            return True
    # Case 2: corner of rect2 inside rect1:
    for corner in rect2corners:
        if rect1.contains(corner):
            return True
    # Case 3: rectangles on top of one another in a cross formation (interiors overlap).
    # Subcases: 1) rect1 horizontal, rect2 vertical
    #           2) rect2 vertical, rect1 horizontal
    # Idea: in either subcase there are four intersection points:
    intersect_1 = Point()
    intersect_2 = Point()
    intersect_3 = Point()
    intersect_4 = Point()

    for i in range(2):
        intersect_1.x = rect2.corner.x
        intersect_1.y = rect1.corner.y

        intersect_2.x = rect2.corner.x + rect2.width
        intersect_2.y = rect1.corner.y

        intersect_3.x = rect2.corner.x
        intersect_3.y = rect1.corner.y + rect1.height

        intersect_4.x = intersect_2.x
        intersect_4.y = intersect_3.y

        intersect_list = [intersect_1, intersect_2, intersect_3, intersect_4]
        for intersect in intersect_list:
            # if these are indeed intersection points, then there is a collision:
            if rect1.contains(intersect) and rect2.contains(intersect):
                return True
        # if subcase 1) fails, swap the two rectangles and compute subcase 2)
        new_rect1 = copy.deepcopy(rect2)
        new_rect2 = copy.deepcopy(rect1)
        rect1 = new_rect1
        rect2 = new_rect2
    return False

# Tests
# Case 1:
rect1 = Rectangle(Point(0,0), 3, 3)
rect2 = Rectangle(Point(1,-1), 1, 3)

test(rect_clash(rect1, rect2) == True)

# Case 2:
rect2 = Rectangle(Point(0,0), 3, 3)
rect1 = Rectangle(Point(1,-1), 1, 3)

test(rect_clash(rect1, rect2) == True)

# Case 3:
rect1 = Rectangle(Point(0,0), 3, 1)
rect2 = Rectangle(Point(1,-1), 1, 3)

test(rect_clash(rect1, rect2) == True)

# Case no clash:
rect1 = Rectangle(Point(0,0), 3, 1)
rect2 = Rectangle(Point(4,-1), 1, 3)

test(rect_clash(rect1, rect2) == False)

