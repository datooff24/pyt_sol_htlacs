import sys


def test(did_pass):
    """  Print the result of a test.  """
    linenum = sys._getframe(1).f_lineno   # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)

################################################################################################################

def hypotenuse(len1, len2):
    """Finds the length of the hypotenuse of a triangle with sides len1, len2 using Pythagoras"""
    side1 = len1**2
    side2 = len2**2
    hypot_square = side1+side2
    hypot = hypot_square**0.5
    return hypot


test(hypotenuse(3, 4) == 5.0)
test(hypotenuse(12, 5) == 13.0)
test(hypotenuse(24, 7) == 25.0)
test(hypotenuse(9, 12) == 15.0)