from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        lp, rp, max_height = 0, len(height) - 1, 0

        while lp < rp:
            current_height = (rp - lp) * min(height[lp], height[rp])
            max_height = max(max_height, current_height)
            if height[lp] < height[rp]:
                lp += 1
            else:
                rp -= 1
        return max_height


result = Solution().maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7])
print(result)
