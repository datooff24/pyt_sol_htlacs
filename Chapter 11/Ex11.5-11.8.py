from TestsChap11 import test

# Ex 11.5
def add_vectors(u, v):
    new_vector = []
    for index in range(len(u)):
        summation = u[index]+v[index]
        new_vector.append(summation)
    return new_vector

test(add_vectors([1, 1], [1, 1]) == [2, 2])
test(add_vectors([1, 2], [1, 4]) == [2, 6])
test(add_vectors([1, 2, 1], [1, 4, 3]) == [2, 6, 4])

# Ex 11.6
def scalar_mult(s, v):
    new_vector = []
    for index in range(len(v)):
        new_element = s*v[index]
        new_vector.append(new_element)
    return new_vector

test(scalar_mult(5, [1, 2]) == [5, 10])
test(scalar_mult(3, [1, 0, -1]) == [3, 0, -3])
test(scalar_mult(7, [3, 0, 5, 11, 2]) == [21, 0, 35, 77, 14])

# Ex 11.7
def dot_product(u, v):
    product = 0
    for index in range(len(u)):
        dot = u[index]*v[index]
        product += dot
    return product

test(dot_product([1, 1], [1, 1]) ==  2)
test(dot_product([1, 2], [1, 4]) ==  9)
test(dot_product([1, 2, 1], [1, 4, 3]) == 12)

# Ex 11.8
def cross_product(u, v):
    #[A1, A2, A3] x [B1, B2, B3] = [(A2*B3) – (A3*B2), (A3*B1) – (A1*B3), (A1*B2) – (A2*B1)]
    new_vector = []
    if len(u) == len(v) and len(u) == 3:
        new_vector.append(u[1]*v[2]-u[2]*v[1])
        new_vector.append(u[2]*v[0]-u[0]*v[2])
        new_vector.append(u[0]*v[1]-u[1]*v[0])
        return new_vector
    else:
        print("vectors need to both have length 3")


test(cross_product([1, 2, 3], [4, 5, 6]) == [-3, 6, -3])
