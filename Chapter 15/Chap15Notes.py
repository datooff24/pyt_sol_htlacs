class Point:
    """Point class represents and manipulates x,y coords. """

    def __init__(self, x=0, y=0):
        """Create a new point at the origin"""
        self.x = x
        self.y = y

    def distance_from_origin(self):
        """Compute my distance from the origin"""
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5


p = Point(4,2)
q = Point(6,3)
r = Point()

print(p.x, q.y, r.x)