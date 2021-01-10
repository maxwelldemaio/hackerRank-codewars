"""
Given an array of integers nums and an integer k, return the total number of continuous subarrays whose sum equals to k.


Example 1:

Input: nums = [1, 1, 1], k = 2
Output: 2
Example 2:

Input: nums = [1, 2, 3], k = 3
Output: 2


Constraints:

1 <= nums.length <= 2 * 104
-1000 <= nums[i] <= 1000
-107 <= k <= 107
"""

from typing import List
from collections import defaultdict

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        n = len(nums)
        sumDict = defaultdict(int) # Dict for the cumulative sums and occurrences
        curr_sum = 0  # Our cumulative sum
        
        for i in range(0, n):
            curr_sum += nums[i]  # Increase cumulative sum
            if curr_sum == k:  # If current cumulative sum is equal to target
                count += 1
            if (curr_sum - k) in sumDict:
                count += sumDict[curr_sum - k]
            # Always add the current cumulative sum to the Dict
            sumDict[curr_sum] += 1
        print(sumDict)
        return count


testing = Solution()
print(testing.subarraySum(nums=[3, 4, 7, 2, -3, 1, 4, 2], k=7))
print(testing.subarraySum(nums=[3, 4, 7, 2, -3, 1, 4, 2, 1], k=7))