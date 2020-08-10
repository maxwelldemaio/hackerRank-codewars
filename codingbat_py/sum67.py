"""
sum67

Return the sum of the numbers in the array, except ignore sections of numbers starting with a 6 and extending to the next 7 
(every 6 will be followed by at least one 7). Return 0 for no numbers.


sum67([1, 2, 2]) → 5
sum67([1, 2, 2, 6, 99, 99, 7]) → 5
sum67([1, 1, 6, 7, 2]) → 4
"""


def sum67(nums):
  ourSum = 0
  sixFoundSeven = True
  if len(nums) == 0:
    return 0
  else:
    for i in range(0, len(nums)):
      if nums[i] == 6:
        sixFoundSeven = False
        continue
      if nums[i] == 7 and sixFoundSeven != True:
        sixFoundSeven = True
        continue
      if sixFoundSeven == True:
        ourSum += nums[i]
    return ourSum
