def print_triangular_numbers(n):
    total = 0
    for i in range(1, n+1):
        total += i
        print(i, "\t", total)


print_triangular_numbers(5)

# ------Alt solution-------

def print_triangular_numbers(n):
    num = 1
    sum = num
    for i in range(n):
        print(num, end="       ")
        print(sum)
        num += 1
        sum += num

print_triangular_numbers(5)
