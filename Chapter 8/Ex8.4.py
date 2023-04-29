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
