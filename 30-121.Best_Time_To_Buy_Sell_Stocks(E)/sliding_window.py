from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i, j = 0, 1
        max_price = 0

        while j < len(prices):
            # when prices of j are higher than prices of i,
            # we keep calculating the max price while iterating j, keeping i at the lower price
            if prices[j] >= prices[i]:
                max_price = max(max_price, prices[j] - prices[i])
                j += 1
            else:
                i = j
                j += 1

        return max_price


result = Solution().maxProfit(prices=[7, 1, 5, 3, 6, 4])
# result = Solution().maxProfit(prices=[7, 6, 4, 3, 1])
print(result)
