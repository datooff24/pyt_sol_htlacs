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


def to_secs(hours, minutes, sec):
    hour2sec = float(hours) * 60 * 60
    min2sec = float(minutes) * 60
    seconds = float(sec)
    total_sec = hour2sec + min2sec + seconds
    return int(total_sec)


test(to_secs(2.5, 0, 10.71) == 9010)
test(to_secs(2.433,0,0) == 8758)

