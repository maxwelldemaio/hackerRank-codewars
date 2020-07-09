"""
In this Kata, we will check if a string contains consecutive letters as they appear in the English alphabet and if each letter occurs only once.

For example: 
solve("abc") = True, because it contains a,b,c
solve("abd") = False, because a, b, d are not consecutive, and c is missing.
solve("dabc") = True, because it contains a, b, c, d
solve("abbc") = False, because b does not occur once.
solve("v") = True
All inputs will be lowercase letters.

More examples in test cases. Good luck!
"""
def solve(st):
    sortedString = sorted(st)

    for x in range(0, len(sortedString) - 1):
        if ord(sortedString[x]) + 1 != ord(sortedString[x + 1]):
            return False 
    return True


print(solve("dabc"))
