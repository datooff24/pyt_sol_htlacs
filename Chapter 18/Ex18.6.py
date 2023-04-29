from Chap18Tests import test
def count(target, lst):
    """gives the number of instances of target in a nested list lst"""
    counter = 0
    for element in lst:
        if type(element) == type([]):
            counter += count(target, element)
        else:
            if element == target:
                counter += 1
    return counter



test(count(2, []) == 0)
test(count(2, [2, 9, [2, 1, 13, 2], 8, [2, 6]]) == 4)
test(count(7, [[9, [7, 1, 13, 2], 8], [7, 6]]) == 2)
test(count(15, [[9, [7, 1, 13, 2], 8], [2, 6]]) == 0)
test(count(5, [[5, [5, [1, 5], 5], 5], [5, 6]]) == 6)
test(count("a",
     [["this",["a",["thing","a"],"a"],"is"], ["a","easy"]]) == 4)
