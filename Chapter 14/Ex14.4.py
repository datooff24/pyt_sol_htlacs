# throughout this exercise, note that for two points (x,y) in a solution bd list, we have y = bd[x] and x = bd.index(y)
# 14.4.a
def mirror_y_axis(bd):
    """mirrors a solution bd in the y-axis"""
    # rotate around y-axis, so y values stay the same
    # if (x,y) is a point in the solution, then the mirrored solution is (len(bd)-1-x,y)

    bd_size = range(len(bd))
    # create list of appropriate length whose entries will edited
    # this is not an empty list because we will be editing the list in random positions, not in order from 0
    result = list(bd_size)
    for x in bd_size:
        result[len(bd) - 1 - x] = bd[x]
    return result


print(mirror_y_axis([1, 3, 0, 2]))


# 14.4.b
def mirror_x_axis(bd):
    """mirrors a solution bd in the x-axis"""
    # rotate around x-axis, so x values stay the same
    # if (x,y) is a point in the solution, then the mirrored solution is (x, len(bd)-1-y)
    bd_size = range(len(bd))
    # empty list because the x-position remains the same, so we can append result in normal order
    result = []
    for x in bd_size:
        y = len(bd) - 1 - bd[x]
        result.append(y)
    return result


print(mirror_x_axis([1, 3, 0, 2]))


# 14.4.c
def rotate_sol_90(bd):
    """rotates a solution bd 90 degrees counterclockwise"""
    # if (x,y) is a point in the solution, then the 90 deg rotated solution is (y, len(bd)-1-x)
    bd_size = range(len(bd))
    result = []
    for y in bd_size:
        y_new = len(bd) - 1 - bd.index(y)
        result.append(y_new)
    return result


print(rotate_sol_90([1, 3, 0, 2]))


def rotate_sol_180(bd):
    """rotates a solution bd 180 deg counterclockwise"""
    # run rotate_sol_90 twice
    result = bd
    for i in range(2):
        result = rotate_sol_90(result)
    return result


def rotate_sol_270(bd):
    # run rotate_sol_90 thrice
    result = bd
    for i in range(3):
        result = rotate_sol_90(result)
    return result

# 14.4.d
# There are two more symmetries left: rotations around the diagonals y=x, y=-x


def mirror_diag(bd):
    """mirrors a solution bd around the diagonal y=x"""
    # because of the coordinate system of the board, y = x has the shape of y = -x in a conventional coordinate system
    # if (x,y) is a point in the solution then the mirrored solution is (y,x) = (y, bd.index(y)
    bd_size = range(len(bd))
    result = []
    for y in bd_size:
        y_new = bd.index(y)
        result.append(y_new)
    return result


def mirror_diag_neg(bd):
    """mirrors a solution bd around the diagonal y = -x"""
    # if (x,y) is a point in the solution, then the mirrored solution is (x,y) = (len(bd)-1-y, len(bd)-1-x)
    #  x = bd.index(y)
    bd_size = range(len(bd))
    result = list(bd_size)
    for y in bd_size:
        result[len(bd)-1-y] = len(bd)-1-bd.index(y)
    return result


# All symmetries have been considered, generate a solution of families now
# Idea: start out with empty result, then append all the solutions from the functions in 14.4.c into result

def sol_fam_of_symmetry(bd):
    """generates a family of symmetries of bd"""
    result = []
    result.append(bd)
    result.append(mirror_x_axis(bd))
    result.append(mirror_y_axis(bd))
    result.append(rotate_sol_90(bd))
    result.append(rotate_sol_180(bd))
    result.append(rotate_sol_270(bd))
    result.append(mirror_diag(bd))
    result.append(mirror_diag_neg(bd))
    return result

# Ex 14.4.e
# First import all the functions to compute solutions

def share_diagonal(x0, y0, x1, y1):
    """ Is (x0, y0) on a shared diagonal with (x1, y1)? """
    dy = abs(y1 - y0)        # Calc the absolute y distance
    dx = abs(x1 - x0)        # Calc the absolute x distance
    return dx == dy          # They clash if dx == dy

def col_clashes(bs, c):
    """ Return True if the queen at column c clashes
         with any queen to its left.
    """
    for i in range(c):     # Look at all columns to the left of c
          if share_diagonal(i, bs[i], c, bs[c]):
              return True

    return False           # No clashes - col c has a safe placement.

def has_clashes(the_board):
    """ Determine whether we have any queens clashing on the diagonals.
        We're assuming here that the_board is a permutation of column
        numbers, so we're not explicitly checking row or column clashes.
    """
    for col in range(1,len(the_board)):
        if col_clashes(the_board, col):
            return True
    return False


# Rough idea for main(n):
# Compute solution and check if it is indeed a solution
# If solution not in symmetry family
#   Compute family of solution
#   Add family to symmetry family
#   Add solution to result

def main(n):
    num_found = 0
    tries = 0
    result = []
    symmetry_fam = []
    while num_found < 10:
        import random
        rng = random.Random()
        bd = list(range(n))
        rng.shuffle(bd)
        tries += 1
        if not has_clashes(bd) and bd not in result:
            if bd not in symmetry_fam:
                symmetry_fam += sol_fam_of_symmetry(bd)
                result.append(bd)
                print("Found solution {0} in {1} tries.".format(bd, tries))
                tries = 0
                num_found += 1


main(8)


