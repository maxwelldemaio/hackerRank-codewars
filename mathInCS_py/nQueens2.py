# Place N queens such that no two attack each other.
# Find the permutation that is the solution for a board size JxJ
# Backtracking

# Check if partial solution can be extended
def can_be_extended_to_solution(perm):
    # Get the last queen
    i = len(perm) - 1
    for j in range(i):
        if i - j == abs(perm[i] - perm[j]):
            return False
    return True


def extend(perm, n):
    # Solution found, length exists
    if len(perm) == n:
        print(perm)
        exit()

    # Try to extend to a new element (new position in curr row)
    for k in range(n):
        # If not in same column (not already in perm we are trying)
        if k not in perm:
            # Try this tree
            perm.append(k)

            if can_be_extended_to_solution(perm):
                extend(perm, n)

            perm.pop()


extend(perm=[], n=20)
