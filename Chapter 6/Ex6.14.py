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


def is_even(n):
    if n % 2 == 0:
        return True
    return False


test(is_even(10))
test(not(is_even(7)))
test(not(is_even(1.4)))
