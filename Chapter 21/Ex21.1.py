from TestsChap21 import test


class MyTime:
    def __init__(self, hrs=0, mins=0, secs=0):
        totalsecs = hrs * 3600 + mins * 60 + secs
        self.hours = totalsecs // 3600
        leftoversecs = totalsecs % 3600
        self.minutes = leftoversecs // 60
        self.seconds = leftoversecs % 60

    def __str__(self):
        return "{0}:{1}:{2}".format(self.hours, self.minutes, self.seconds)

    def to_seconds(self):
        return self.hours * 3600 + self.minutes * 60 + self.seconds


def between(t1, t2, obj):
    t1_sec = t1.to_seconds()
    t2_sec = t2.to_seconds()
    obj_sec = obj.to_seconds()
    if t1_sec <= obj_sec < t2_sec:
        return True
    else:
        return False


t1 = MyTime(13, 15, 53)
obj = MyTime(13, 19, 44)
t2 = MyTime(15, 50, 59)

test(between(t1, t2, obj))
