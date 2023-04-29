from TestsChap8 import test


def count(substring, string):
    start = 0
    counter = 0
    while start < len(string):
        if string.find(substring, start) != -1:
            counter += 1
            start = string.find(substring, start) + 1
        else:
            break
    return counter


test(count("is", "Mississippi") == 2)
test(count("an", "banana") == 2)
test(count("ana", "banana") == 2)
test(count("nana", "banana") == 1)
test(count("nanan", "banana") == 0)
test(count("aaa", "aaaaaa") == 4)