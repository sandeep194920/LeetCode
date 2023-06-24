"""
Example -> [2,7,11,15], target = 18 -> [1,2]

Let's say I have two pointers (left at start and right at end). I'll add them up and
if result is more than target that means I need to decrease the numbers, so I will move my right pointer
to left (this means I am decreasing the numbers as they are sorted), and in that way I am moving closer to
target. Similarly, if the addition of numbers is less than target then I'll move my left pointer towards
right increasing the addition towards target. That's the idea.

"""
from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        lp, rp = 0, len(numbers) - 1

        while lp < rp:

            sum_of_nums = numbers[lp] + numbers[rp]

            # we can add an elif and then this if condition can be at else part. Either way it is same
            if sum_of_nums == target:
                return [lp+1, rp+1]

            if sum_of_nums > target:
                rp -= 1
            else:
                lp += 1

        return []


result = Solution()
print(result.twoSum([2, 7, 11, 15], 18))
