def swap(x, y):
    (x, y) = (y, x)
    return x, y

a = ["This", "is", "fun"]
b = [2, 3, 4]
print("before swap function call: a:", a, "b:", b)
a, b = swap(a, b)
print("after swap function call: a:", a, "b:", b)
