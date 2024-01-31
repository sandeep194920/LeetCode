import math
from typing import List


class Solution:
    def search(self, nums: List[int], key: int) -> int:
        start = 0
        end = len(nums) - 1

        while start <= end:
            mid = math.floor(start + (end - start) / 2)
            if nums[mid] == key:
                return nums[mid]
            elif nums[mid] < key:
                start = mid + 1
            else:
                end = mid - 1
        # at this point if the key is not found, then the high and low would have crossed each other
        low = nums[end]
        high = nums[start]
        return min(low, high)


result = Solution().search(nums=[1, 3, 8, 10, 15], key=12)  # output 2
# result = Solution().search([1, 3, 8, 10, 12, 15], key=12)  # output 0

print(result)
