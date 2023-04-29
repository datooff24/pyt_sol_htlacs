from TestsChap7 import test

def num_even_digits(number):
    count = 0
    for digit in str(number):
        if digit in "02468":
            count += 1
    return count


test(num_even_digits(123456) == 3)
test(num_even_digits(2468) == 4)
test(num_even_digits(1357) == 0)
test(num_even_digits(0) == 1)


