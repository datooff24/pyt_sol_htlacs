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


# Exercise 9(a)
def hours_in(sec):
    hours = int(sec) / 3600
    return int(hours)


# Exercise 9(b)
def minutes_in(sec):
    seconds = int(sec) % 3600
    minutes = seconds / 60
    return int(minutes)


# Exercise 9(c)
def seconds_in(sec):
    seconds = int(sec) % 3600
    seconds_left = seconds % 60
    return seconds_left


test(hours_in(9010) == 2)
test(minutes_in(9010) == 30)
test(seconds_in(9010) == 10)





