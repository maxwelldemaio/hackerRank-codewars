# Moving Zeros To The End
"""
Write an algorithm that takes an array and moves all of the zeros to the end, 
preserving the order of the other elements.

move_zeros([False,1,0,1,2,0,1,3,"a"]) # returns[False,1,1,2,1,3,"a",0,0]
"""


def move_zeros(array):
    index = 0
    for x in range(0, len(array)):
        # Place number at index if not zero
        if array[x] is False:
            array[index] = array[x]
            index += 1
        if array[x] != 0:
            array[index] = array[x]
            index += 1
    # Populate zeros at end
    for x in range(index, len(array)):
        array[x] = 0

    return array

# Test case
assert move_zeros([False, 1, 0, 1, 2, 0, 1, 3, "a"]) == [False, 1, 1, 2, 1, 3, "a", 0, 0]
