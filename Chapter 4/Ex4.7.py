def sum_to(n):
    """Sums the integers from 0 up to and including n"""
    total = 0
    for i in range(n+1):
        total = total+i
    return total


print(sum_to(10))