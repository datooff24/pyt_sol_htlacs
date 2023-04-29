from TestsChap14 import test

# 14.1.a

def merge_a(xs, ys):
    """ merge elements that are in both xs and ys from ordered lists xs and ys. """
    result = []
    xi = 0
    yi = 0
    while True:
        if xi >= len(xs):  # If xs list is finished
            return result
        if yi >= len(ys):  # If ys list is finished
            return result
        if xs[xi] == ys[yi]:
            # add the element to the list
            result.append(xs[xi])
            # go to the next item
            xi += 1
        elif xs[xi] < ys[yi]:
            # then xs[xi] < ys[yi+1] etc. since the lists are ordered
            # so xs[xi] is not in both lists, go to the next item
            xi += 1
        elif xs[xi] > ys[yi]:
            # then maybe xs[xi] is equal to the next element in ys, so increase yi and check if equality now holds
            yi += 1

test(merge_a([1,2,3,4], [1,4,5,6]) == [1,4])
test(merge_a([4,9,10], [1,4,5,6]) == [4])
test(merge_a(["A", "B", "d", "f"], ["a", "b", "c", "d", "e", "f"]) == ["d", "f"])

#--------------------------------------------------------------------------------------------------------------------

# 14.1.b
def merge_b(xs, ys):
    """ merge elements that are only in xs and not in ys from sorted lists xs and ys  """
    result = []
    xi = 0
    yi = 0
    while True:
        if xi >= len(xs):  # If xs list is finished
            return result
        if xs[xi] == ys[yi]:
            # then xs[xi] does not belong in result, move to xs[xi+1]
            xi += 1
        elif xs[xi] < ys[yi]:
            # then xs[xi] < ys[yi+1] etc. so xs[xi] is not in both lists, add to result
            result.append(xs[xi])
            # move to next item
            xi += 1
        elif xs[xi] > ys[yi]:
            # if one element in xs is larger than all the elements in ys, then the remaining
            # elements in xs will also be larger than ys, hence will not be in ys
            if xs[xi] > ys[len(ys)-1]:
                result.extend(xs[xi:])
                return result
            # increase yi until == or < has been reached
            yi += 1

test(merge_b([1,2,3,4], [1,4,5,6]) == [2,3])
test(merge_b([4,9,10], [1,4,5,6]) == [9, 10])
test(merge_b(["A", "B", "d", "f"], ["a", "b", "c", "d", "e", "f"]) == ["A", "B"])

# --------------------------------------------------------------------------------------------------------------------

# 14.1.c
def merge_c(xs, ys):
    """ merge elements that are only in ys and not in xs from sorted lists xs and ys  """
    result = []
    xi = 0
    yi = 0
    while True:
    # same as in merge_b, but swap x and y.
        if yi >= len(ys):  # If ys list is finished
            return result
        if xs[xi] == ys[yi]:
            yi += 1
        elif xs[xi] > ys[yi]:
            result.append(ys[yi])
            yi += 1
        elif xs[xi] < ys[yi]:
            if ys[yi] > xs[len(xs)-1]:
                result.extend(ys[yi:])
                return result
            # increase xs[xi] until == or < has been reached
            xi += 1


test(merge_c([1,2,3,4], [1,4,5,6]) == [5,6])
test(merge_c([4,9,10], [1,4,5,6]) == [1,5,6])
test(merge_c(["A", "B", "d", "f"], ["a", "b", "c", "d", "e", "f"]) == ["a", "b", "c", "e"])

# -----------------------------------------------------------------------------------------------------------------

# 14.1.d
def merge_d(xs, ys):
    """ merge elements that are in either xs or ys """
    result = []
    xi = 0
    yi = 0
    while True:
        if xi >= len(xs):
            for item in ys[yi:]:  # only include the remaining items that are not already in result
                if item not in result:
                    result.append(item)
            return result
        if yi >= len(ys):
            for item in xs[xi:]:  # only include the remaining items that are not already in result
                if item not in result:
                    result.append(item)
            return result
        if xs[xi] <= ys[yi]:
            if xs[xi] not in result:  # only append the item if it is not in result to avoid duplicates
                result.append(xs[xi])
            xi += 1
        elif xs[xi] > ys[yi]:
            if ys[yi] not in result:  # only append the item if it is not in result to avoid duplicates
                result.append(ys[yi])
            yi += 1

test(merge_d([1,2,3,4], [1,4,5,6]) == [1,2,3,4,5,6])
test(merge_d([4,9,10], [1,4,5,6]) == [1,4,5,6,9,10])
test(merge_d(["A", "B", "d", "f"], ["a", "b", "c", "d", "e", "f"]) == ["A", "B", "a", "b", "c", "d", "e", "f"])

# ------------------------------------------------------------------------------------------------------------------

def merge_e(xs, ys):
    """Return items from the first list that are not eliminated by a matching element in the second list. In this case,
     an item in the second list “knocks out” just one matching item in the first list."""
    result = []
    xi = 0
    yi = 0
    while True:
        if xi >= len(xs):
            result.extend(ys[yi:])
            return result
        if yi >= len(ys):
            result.extend(xs[xi:])
            return result
        if xs[xi] < ys[yi]:
            result.append(xs[xi])
            xi += 1
        elif xs[xi] > ys[yi]:
            yi += 1
        elif xs[xi] == ys[yi]:  # Knock out element from both lists
            xi += 1
            yi += 1

test(merge_e([5,7,11,11,11,12,13], [7,8,11]) == [5,11,11,12,13])
test(merge_e(["a", "a", "b", "b", "b", "c"], ["a", "b", "c", "d"]) == ["a", "b", "b", "d"])
