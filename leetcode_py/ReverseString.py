# Reverse String
"""
Write a function that reverses a string. 
The input string is given as an array of characters char[].

Do not allocate extra space for another array, you must do this by 
modifying the input array in-place with O(1) extra memory.

You may assume all the characters consist of printable ascii characters.


Example 1:

Input: ["h","e","l","l","o"]
["o","l","l","e","h"]


["o","l","l","e","h"]

Output: ["o","l","l","e","h"]
Example 2:

Input: ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]
"""

class Solution:
    def reverseString(self, s):
        # Setup the left and right pointer
        left, right = 0, len(s) - 1
        # Left pointer will increment while right decrements
        while left < right:
            # Swap
            s[left], s[right] = s[right], s[left]
            # Increment left pointer decrement right pointer
            left, right = left + 1, right - 1


# Create solution instance
l = Solution()

a = ["h", "i"]
b = ['t', 'h', 'i', 's', 'i', 's', 'm', 'a', 'x']

# Tests (Lists are mutuable so technically changes the original list)
l.reverseString(a)
l.reverseString(b)

print(a)
print(b)
