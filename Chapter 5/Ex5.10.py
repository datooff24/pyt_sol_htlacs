def find_hypot(len1, len2):
    """Finds the length of the hypotenuse of a triangle with sides len1, len2 using Pythagoras"""
    side1 = len1**2
    side2 = len2**2
    hypot_square = side1+side2
    hypotenuse = hypot_square**0.5
    return hypotenuse


print(find_hypot(3, 4))
