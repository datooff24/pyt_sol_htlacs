from TestsChap7 import test


def sum_list_partial(lists):
    sum = 0
    for item in lists:
        if item % 2 == 0:
            break
        else:
            sum += item
    return sum


test(sum_list_partial([1,3,5]) == 9)