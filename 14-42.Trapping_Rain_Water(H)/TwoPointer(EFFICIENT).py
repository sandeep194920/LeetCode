from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:

        lhb = height[0]
        rhb = height[len(height) - 1]
        lp, rp = 0, len(height) - 1
        total_water = 0

        while lp <= rp:
            if lhb <= rhb:  # if lhb is less or equal to rhb, then the water level will be equal to lhb
                if height[lp] >= lhb:
                    lhb = height[lp]
                else:
                    tw = lhb - height[lp]
                    total_water += tw

                lp += 1

            else:  # if rhb is less, then the water level will be equal to rhb
                if height[rp] > rhb:
                    rhb = height[rp]
                else:
                    tw = rhb - height[rp]
                    total_water += tw

                rp -= 1

        return total_water


result = Solution().trap([4, 2, 0, 3, 2, 5])
# result = Solution().trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1])
print(result)
