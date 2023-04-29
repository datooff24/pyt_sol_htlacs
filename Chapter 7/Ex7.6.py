from TestsChap7 import test


def count_word_partial(lists):
    counter = 0
    for item in lists:
        counter += 1
        if item == "Sam":
            break
    return counter


test(count_word_partial(["Peter", "Sam"]) == 2)
