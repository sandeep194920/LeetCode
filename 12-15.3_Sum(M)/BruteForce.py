"""
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]

We will use 3 pointers (3 for-loops), but it's not the logic of actual 3 pointers concept.
That is in Threepointer.py
"""

# THIS SOLUTION WON'T WORK AS THE TIME EXCEEDS

from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        combinations = []
        nums = sorted(nums)
        for i in range(len(nums) - 2):
            for j in range(i + 1, len(nums) - 1):
                for k in range(j + 1, len(nums)):
                    if nums[i] + nums[j] + nums[k] == 0 and [nums[i], nums[j], nums[k]] not in combinations:
                        combinations.append([nums[i], nums[j], nums[k]])

        return combinations


print(Solution().threeSum([-4, -1, -1, 0, 1, 2]))
# Solution().threeSum([-1, 0, 1, 2, -1, -4])
