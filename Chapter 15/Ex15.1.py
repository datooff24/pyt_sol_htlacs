class Point:
    """Point class represents and manipulates x,y coords. """

    def __init__(self, x=0, y=0):
        """Create a new point at the origin"""
        self.x = x
        self.y = y

def distance(p, q):
    dx = q.x - p.x
    dy = q.y - p.y
    dsquared = dx*dx + dy*dy
    result = dsquared**0.5
    return result

