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


def is_odd(n):
    if is_even(n):
        return False
    elif n % 2 == 1:
        return True


test(not(is_odd(10)))
test(is_odd(7))
test(not(is_odd(1.4)))
