def count_letters(string, letter, start=0):
    count = 0
    while start < len(string):
        if string.find(letter, start) != -1:
            count += 1
            start = string.find(letter, start) + 1
        else:
            break
    return count


print(count_letters("banana", "a"))


#-----Alt solution-----
# Idea:
# find method gives the position of the FIRST occurrence of the letter
# call find method to find the first occurrence
# call find method again, starting one spot after the position of the found letter
# repeat until the start position is too large to be possible to be used


def count_letters(strng, letter, start=0):
    count = 0
    while start < len(strng):
        position = strng.find(letter, start)
        if position == -1:
            return count
        else:
            count += 1
            start = position+1
    return count


print(count_letters("banana", "a"))
