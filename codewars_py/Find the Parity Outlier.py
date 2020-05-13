"""
You are given an array (which will have a length of at least 3, but could be very large) containing integers. 
The array is either entirely comprised of odd integers or entirely comprised of even integers except 
for a single integer N. Write a method that takes the array as an argument and returns this "outlier" N.

Examples:
[2, 4, 0, 100, 4, 11, 2602, 36]
Should return: 11 (the only odd number)

[160, 3, 1719, 19, 11, 13, -21]
Should return: 160 (the only even number)
"""

def find_outlier(integers):
    test = 0
    # Test whether the list is evens or odds by looking at first 3 values
    for i in range(0, 3):
        test += integers[i] % 2
    
    # If string was full of odds, look for even number
    if test >= 2:
        for x in integers:
            if x % 2 == 0:
                return x
    # Look for odd number
    else:
        for y in integers:
            if y % 2 == 1:
                return y
