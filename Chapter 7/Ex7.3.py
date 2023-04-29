def sum_negative(n):
    total_sum = 0
    for item in n:
        if item < 0:
            total_sum = total_sum + item
    return total_sum
