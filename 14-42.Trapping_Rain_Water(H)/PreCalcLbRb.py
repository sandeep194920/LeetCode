"""
Approach - We will pre-calculate leftmost highest bar and rightmost highest bar

Calculate the LB and RB even before looping from 2nd element to 2nd last element. This would
make it run in O(N) time

LBs    =  4  4  4  4  4  5

height =  4  2  0  3  2  5

RBs    =  5  5  5  5  5  5

"""

from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:

        total_water = 0

        # let's first calculate LB and RB for each bar
        lb, rb = [0] * len(height), [0] * len(height)
        lb[0] = height[0]
        rb[len(height) - 1] = height[len(height) - 1]

        for i in range(1, len(height)):
            lb[i] = max(lb[i - 1], height[i])

        for i in range(len(height) - 2, -1, -1):
            rb[i] = max(height[i], rb[i + 1])

        for i in range(1, len(height) - 1):
            wl = min(lb[i], rb[i])
            tw = wl - height[i]
            total_water += tw

        return total_water


result = Solution().trap([4, 2, 0, 3, 2, 5])
print(result)
