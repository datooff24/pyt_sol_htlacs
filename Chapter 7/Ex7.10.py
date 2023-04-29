from TestsChap7 import test

def is_prime(n):
    if n == 1:
        return False
    elif n == 2:
        return True
    else:
        for i in range(2, n):
            if n % i == 0:
                return False
        return True


test(is_prime(11))
test(not is_prime(35))
test(is_prime(19911121))

