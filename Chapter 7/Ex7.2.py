def sum_even(n):
    total_sum = 0
    for item in n:
        if item % 2 == 0:
            total_sum = total_sum + item
    return total_sum