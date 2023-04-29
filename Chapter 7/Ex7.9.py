def print_triangular_numbers(n):
    total = 0
    for i in range(1, n+1):
        total += i
        print(i, "\t", total)


print_triangular_numbers(5)