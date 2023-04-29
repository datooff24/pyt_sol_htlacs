def is_rightangled(len1, len2, len3):
    """Determines if a triangle is right-angled by checking if Pythagoras holds"""
    side1 = len1 ** 2
    side2 = len2 ** 2
    side3 = len3 ** 2
    if abs(side3-(side1+side2)) < 0.000001 or abs(side2-(side1+side3)) < 0.000001 or \
            abs(side1-(side3+side2)) < 0.000001:
        return True
    else:
        return False


print(is_rightangled(5, 3, 4))
