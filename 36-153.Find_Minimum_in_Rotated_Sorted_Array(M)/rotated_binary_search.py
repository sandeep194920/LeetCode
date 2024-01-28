import math
from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        start, end = 0, len(nums) - 1
        while start <= end:
            mid = math.floor(start + (end - start) / 2)

            next_index = (mid + 1) % len(nums)
            prev_index = (mid - 1 + len(nums)) % len(nums)

            if nums[prev_index] > nums[mid] and nums[mid] < nums[next_index]:
                return nums[mid]
            elif nums[mid] > nums[end]:
                start = mid + 1
            else:
                end = mid - 1
        # if there is 1 element in the array, while loop is not executed, so we need to return here
        # note that, as per the constraints, we can't have 0 elements in array
        return nums[0]

    # result = Solution().findMin([3, 4, 5, 1, 2])


# result = Solution().findMin([4, 5, 6, 7, 0, 1, 2])
# result = Solution().findMin([11, 13, 15, 17])
result = Solution().findMin([1])
print(result)
