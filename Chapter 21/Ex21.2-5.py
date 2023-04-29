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

    # Ex 21.2
    def between(self, t1, t2):
        t1_sec = t1.to_seconds()
        t2_sec = t2.to_seconds()
        obj_sec = self.to_seconds()
        if t1_sec <= obj_sec < t2_sec:
            return True
        else:
            return False

    # Ex 21.3
    def __gt__(self, other):
        if self.to_seconds() > other.to_seconds():
            return True
        else:
            return False

    # Ex 21.4
    def increment(self, other):
        # convert object to seconds
        sec = self.to_seconds()
        # add increment to object
        total_sec = sec + other
        # convert back to time object
        return MyTime(0, 0, total_sec)


t1 = MyTime(13, 15, 53)
obj = MyTime(13, 19, 44)
t2 = MyTime(15, 50, 59)

test(obj.between(t1, t2))
test(t2 > t1)

# Ex 21.5
print(t1.increment(-1))
print(t1.increment(-54))
