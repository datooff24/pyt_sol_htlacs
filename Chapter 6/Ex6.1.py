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

def turn_clockwise(point):
    if point == "N":
        return "E"
    elif point == "E":
        return "S"
    elif point == "S":
        return "W"
    elif point == "W":
        return "N"


test(turn_clockwise("N") == "E")
test(turn_clockwise("W") == "N")
test(turn_clockwise(42) == None)
test(turn_clockwise("rubbish") == None)
