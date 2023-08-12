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


def is_factor(f, n):
    """Determines if f divides n"""
    if n / f == int(n / f):
        return True
    else:
        return False


def is_multiple(a, b):
    if is_factor(b, a):
        return True
    else:
        return False


test(is_multiple(12, 3))
test(is_multiple(12, 4))
test(not is_multiple(12, 5))
test(is_multiple(12, 6))
test(not is_multiple(12, 7))
