from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        # Make nums in ascending order
        nums.sort()
        size = len(nums)

        for i in range(size - 2):
            # Make sure no duplicates exists for i
            if i > 0 and nums[i]==nums[i-1]:
                continue

            # Setup pointers
            l = i + 1
            r = size - 1

            while l < r:
                total = nums[i] + nums[l] + nums[r]
                if total < 0:
                    l = l + 1
                elif total > 0:
                    r = r -1
                else:
                    ans.append([nums[i], nums[l], nums[r]])
                    # Make sure no duplicates for l/r
                    # After finding a right answer
                    while l < r and nums[l] == nums[l+1]:
                        l = l + 1
                    while l < r and nums[r] == nums[r - 1]:
                        r = r -1
                    l = l + 1
                    r = r - 1    
        return ans

test = Solution()

print(test.threeSum([-2, -1, 0, 1]))
print(test.threeSum([-1, 0, 1, 2, -1, 4]))
