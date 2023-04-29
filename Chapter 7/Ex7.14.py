from TestsChap7 import test


def num_digits(n):
    count = 0
    if n == 0:
        return 1
    else:
        if n < 0:
            n = abs(n)
        while n != 0:
            count = count + 1
            n = n // 10
    return count


test(num_digits(0) == 1)
test(num_digits(-12345) == 5)
