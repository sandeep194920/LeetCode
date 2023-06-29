"""
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1].
 In this case, 6 units of rain water (blue section) are being trapped.
"""

# THIS SOLUTION WON'T WORK FOR A FEW EDGE CASES - SO DON'T CONSIDER THIS APPROACH


from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:

        total_water = 0
        lp, rp = 0, 0
        stop = False

        if len(height) < 2:
            return 0

        while height[lp] <= 0:
            lp += 1
        rp = lp + 1

        while rp < len(height):

            while height[rp] < height[lp] and rp < len(height) - 1:
                rp += 1

            # if rp == len(height) - 1 and height[rp] < height[rp - 1]:
            #     stop = True
            #     rp = rp - 1

            current_water = (rp - lp - 1) * min(height[lp], height[rp])

            # remove obstacles
            # lp -> 3, rp = 7 (we need from 4 to 6 as obstacles would be here)
            temp_lp = lp + 1
            while temp_lp < rp:
                current_water = current_water - min(height[temp_lp], height[rp])
                temp_lp += 1

            total_water += current_water

            lp = rp
            rp = lp + 1

        return max(total_water, 0)


result = Solution().trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1])
# result = Solution().trap([4, 2, 0, 3, 2, 5])
# result = Solution().trap([5, 4, 1, 2])
# result = Solution().trap([5, 5, 1, 7, 1, 1, 5, 2, 7, 6])
print(result)
