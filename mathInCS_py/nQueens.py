# Place N queens such that no two attack each other.
# Find the permutation that is the solution for a board size JxJ
# Brute force

import itertools as it

def is_solution(perm):
    for (i1, i2) in it.combinations(range(len(perm)), 2):
        if abs(i1 - i2) == abs(perm[i1] - perm[i2]):
            return False
    return True


# Check two for J = 8
for perm in it.permutations(range(4)):
    if is_solution(perm):
        print(perm)
        exit()
