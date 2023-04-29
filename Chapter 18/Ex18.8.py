def fibonacci(n):
    val = 0
    if n == 0:
         return 0
    if n == 1:
         return 1
    else:
        n0 = 0
        n1 = 1
        for i in range(2,n+1):
            val = n1 + n0
            n0 = n1
            n1 = val
        return val

print(fibonacci(200))