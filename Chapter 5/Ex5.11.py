def is_rightangled(len1, len2, len3):
    """Determines if a triangle is right-angled by checking if Pythagoras holds"""
    side1 = len1 ** 2
    side2 = len2 ** 2
    hypot_square = side1 + side2
    hypotenuse = hypot_square ** 0.5
    if abs(len3-hypotenuse) < 0.000001:
        return True
    else:
        return False


print(is_rightangled(3, 4, 5))
