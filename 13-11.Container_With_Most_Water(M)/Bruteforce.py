"""
Bruteforce approach - Let's solve first using BF approach.
I won't this to actually execute the leetcode as it might time out (but I'll try for first input on leetcode
"""
from typing import List


class Solution:
    @staticmethod
    def maxArea(height: List[int]) -> int:
        max_height = 0
        for i in range(0, len(height)):
            for j in range(i + 1, len(height)):
                current_height = (j - i) * min(height[i], height[j])
                max_height = max(current_height, max_height)
        return max_height


result = Solution().maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7])
print(result)
