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

def f2c(t):
    """converts t fahrenheit to celsius"""
    # C = (F - 32) * 5 / 9
    celsius = (t - 32) * 5 / 9
    return round(celsius)

test(f2c(212) == 100) 
test(f2c(32) == 0)
test(f2c(-40) == -40)
test(f2c(36) == 2)
test(f2c(37) == 3)
test(f2c(38) == 3)
test(f2c(39) == 4)


