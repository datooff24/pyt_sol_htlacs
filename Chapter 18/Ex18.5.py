from Chap18Tests import test
def recursive_min(lst):
    """
      Find the minimum in a recursive structure of lists
      within other lists. Precondition: No lists or sublists are empty.
    """
    minimum = None
    first_time = True
    for element in lst:
        if type(element) == type([]):
            value = recursive_min(element)
        else:
            value = element

        if first_time or value < minimum:
            minimum = value
            first_time = False

    return minimum

test(recursive_min([2, 9, [1, 13], 8, 6]) == 1)
test(recursive_min([2, [[100, 1], 90], [10, 13], 8, 6]) == 1)
test(recursive_min([2, [[13, -7], 90], [1, 100], 8, 6]) == -7)
test(recursive_min([[[-13, 7], 90], 2, [1, 100], 8, 6]) == -13)