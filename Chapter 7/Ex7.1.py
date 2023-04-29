def how_many_odd(n):
    counter = 0
    for item in n:
        if item % 2 == 1:
            counter += 1
    return counter
