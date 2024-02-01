import math
from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        start, end = 1, max(piles)
        k_bananas = max(piles)
        while start <= end:
            k_bananas_candidate = math.floor(start + (end - start) / 2)
            hours_taken = self.check_hours_taken(k_bananas_candidate, piles)
            if hours_taken <= h:
                k_bananas = min(k_bananas, k_bananas_candidate)
                end = k_bananas_candidate - 1
            else:
                start = k_bananas_candidate + 1

        return k_bananas

    def check_hours_taken(self, mid, piles):
        hours_taken = 0
        for pile in piles:
            hours_taken += math.ceil(pile / mid)
        # hours_taken = sum(math.ceil(pile / mid) for pile in piles)
        return hours_taken


# result = Solution().minEatingSpeed([3, 6, 7, 11], h=8)  # 4
# result = Solution().minEatingSpeed([30, 11, 23, 4, 20], h=5)  # 30
# result = Solution().minEatingSpeed([30, 11, 23, 4, 20], h=6)  # 23
# result = Solution().minEatingSpeed([312884470], h=312884469)  # 2
result = Solution().minEatingSpeed([3], h=312884469)  # 2
print(result)
