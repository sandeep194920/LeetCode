import math
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1

        while start <= end:
            mid = math.floor(start + (end - start) / 2)
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                start = mid + 1
            else:
                end = mid - 1
        return -1


# result = Solution().search(nums=[-1, 0, 3, 5, 9, 12], target=9)  # output 4
result = Solution().search([-1, 0, 3, 5, 9, 12], target=2)  # output -1

print(result)
