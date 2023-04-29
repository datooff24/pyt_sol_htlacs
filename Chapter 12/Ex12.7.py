from TestsChap12 import *

def myreplace(old, new, s):
    """ Replace all occurrences of old with new in s. """
    if old == " ":
        new_item = new.join(s.split())
    else:
        new_item = new.join(s.split(old))
    return new_item

test(myreplace(",", ";", "this, that, and some other thing") ==
                         "this; that; and some other thing")
test(myreplace(" ", "**",
                 "Words will now      be  separated by stars.") ==
                 "Words**will**now**be**separated**by**stars.")