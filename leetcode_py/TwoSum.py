# Two Sum

"""
Given an array of integers nums and an integer target, return indices of 
the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, 
and you may not use the same element twice.

You can return the answer in any order.

 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
 

Constraints:

2 <= nums.length <= 105
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.
"""

# Brute force solution 
class Solution1:
    def twoSum(self, nums, target):
        # Loop over each item in nums
        for i in range(len(nums)):
            # Check every item's sum with other items
            for j in range(i + 1, len(nums)):
                # If the sum of the current num and the other item equals target
                if nums[i] + nums[j] == target:
                    # Add index of solutions to a list
                    targetList = [i, j]
                    return targetList


# Hashmap solution
class Solution2:
    def twoSum(self, nums, target):
        compHash = {}
        for index, num in enumerate(nums):
            # Add compliment to hashmap
            if compHash.get(num) is None:
                compHash[target - num] = index
            else:
                # Solution found
                result = [compHash[num], index]
        return result

# Create solution instance
l = Solution2()

# Tests
print(l.twoSum([3,2,4], 6))
print(l.twoSum([2, 7, 11, 15], 9))
