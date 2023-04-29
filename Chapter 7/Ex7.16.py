from TestsChap7 import test


def sum_of_squares(xs):
    count = 0
    for number in xs:
        count += number**2
    return count


test(sum_of_squares([2, 3, 4]) == 29)
test(sum_of_squares([]) == 0)
test(sum_of_squares([2, -3, 4]) == 29)