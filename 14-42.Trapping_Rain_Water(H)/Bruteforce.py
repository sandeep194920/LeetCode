"""
- At every bar, we need to calculate water level (WL), and to do this we need to calculate left and right boundary,
LB and RB
- REMEMBER, this LB and RB calculation can start from 2nd element to 2nd last element as we know that the left most bar
  (first bar) would not store any water as there are no bars to it’s left, and similarly the right most bar (last bar)
  wouldn't store any water as there are no bars to it’s right.
- ALSO REMEMBER that, this calculation of finding the left and right boundary, LB and RB must be done at each bar to
  calculate the water level (WL) at that particular bar and then subtracting whatever the bar height at that point is.
- The reason for calculating the LB and RB at each point is
    - because we need min height of those two ofcourse to find the water level
    - and also because, these boundaries might change for bars as we traverse
        - Let’s consider this example here

            [4   0    5   1   6 ]

        - At element 0 (2nd element), the LB is 4, and RB is 6
        - At element 5 the LB is still 4 and RB is 6
        - But at element 1, the LB is 5 and not 4 anymore as this 5 now is greater than 4
        - So this concludes that we need to calculate LB and RB at every bar
"""
from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:

        total_trapped_water = 0

        # Since wkt the left most and right most bars won't trap water, we will start from 2nd till 2nd last elements
        for i in range(1, len(height) - 1):

            # now to start with, i will be at 1 fist time, and we need to calculate lb and rb
            # first we can initialize lb and rb with 2nd and 2nd last elements
            lb = height[i]
            rb = height[i]  # initially assuming both left and right boundaries to be same element (2nd element)

            # find the leftmost highest bar lb from the current position
            for j in range(0, i):  # 0 to i but not including i (0 to 1 element less than i)
                lb = max(height[j], lb)

            # similarly find the rightmost highest bar from the current i+1 position
            for j in range(i + 1, len(height)):
                rb = max(height[j], rb)

            # at this point, we have found the LB and RB for this particular i value

            # Now let's find the water level (max height a water can be stored if no bars(obstacles) )
            wl = min(lb, rb)

            # Since we know the water level, let's calculate trapped water (tw) which will be water level - bar's height
            tw = wl - height[i]

            # Now we can update the total water trapped by adding this tw to total water
            total_trapped_water += tw

        return total_trapped_water


result = Solution().trap([4, 2, 0, 3, 2, 5])
print(result)
