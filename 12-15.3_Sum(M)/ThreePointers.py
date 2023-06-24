"""
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]

We will now solve this using technique we used in 2 sum II (2 pointer approach), but using 3 pointers instead
as we need 3 numbers
"""

from typing import List


def threeSum(nums: List[int]) -> List[List[int]]:
    combinations = []
    # nums = sorted(nums)
    nums.sort()
    for i in range(len(nums) - 2):

        # this if check is optional (but increases the efficiency) and avoids duplicate checks
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        lp = i + 1
        rp = len(nums) - 1
        while lp < rp:
            current_sum = nums[i] + nums[lp] + nums[rp]

            if current_sum > 0:
                rp = rp - 1
            elif current_sum < 0:
                lp = lp + 1
            else:
                combinations.append([nums[i], nums[lp], nums[rp]])
                lp = lp + 1
                while nums[lp] == nums[lp - 1] and lp < rp:
                    lp = lp + 1

    return combinations


# print(threeSum([-4, -1, -1, 0, 1, 2]))
# print(threeSum([-3, -3, 1, 2, 3, 4]))
print(threeSum([-2, -2, 0, 0, 2, 2]))
