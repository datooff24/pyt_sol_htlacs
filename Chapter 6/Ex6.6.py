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


def days_in_month(month):
    """Tells us the number of days the inserted month has"""
    days_31 = ["January", "March", "May", "July", "August", "October", "December"]
    days_30 = ["April", "June", "September", "November"]
    if month in days_31:
        return 31
    elif month in days_30:
        return 30
    elif month == "February":
        return 28

test(days_in_month("February") == 28)
test(days_in_month("December") == 31)
