"""
# Maximum-Subarray-Sum

## Description
The maximum sum subarray problem consists in 
finding the maximum sum of a contiguous subsequence in an array or list of integers

Ex)
max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4])
(should be 6): [4, -1, 2, 1]

Easy case is when the list is made up of only 
positive numbers and the maximum sum is the sum of the whole array. 
If the list is made up of only negative numbers, return 0 instead.

Empty list is considered to have zero greatest sum. 
Note that the empty list or array is also a valid sublist/subarray.

## Solution
We could brute force the solution and try and find the maximum subarray at iterating 
through each index and checking every possible solution. 
This would result in a time complexity of O(n^2).

### The implementation I will use will be Kadane's Algorithm.
We look at each index and ask, what's the maximum subarray ending at this index?

Ex)
[1, -3, 2, 1, -1]
should be: [1] [1, -3] [2] [3] ...
"""

def max_sequence(arr):
    # If list is empty, return 0
    if not arr:
        return 0
    
    # Maximum subarray at array[x] will either be x
    # Or x plus the maximum subarray @ the previous index
    current_max = global_max = arr[0]
    for x in range(1, len(arr)):
        current_max = max(arr[x], current_max + arr[x])
        if current_max > global_max:
            global_max = current_max
        
    # If all numbers negative, return 0
    if global_max < 0:
        return 0
        
    return global_max

print(max_sequence([1,2,3]))
print(max_sequence([-2,3,2,-1]))
print(max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
print(max_sequence([-1, -2, -3]))
print(max_sequence([]))
