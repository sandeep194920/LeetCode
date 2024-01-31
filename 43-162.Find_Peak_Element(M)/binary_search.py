import math
from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        start, end = 0, len(nums) - 1
        while start <= end:

            # # edge cases

            # if only one element exists, then that is the peak
            if len(nums) == 1:
                return 0

            mid = math.floor(start + (end - start) / 2)

            # # compare mid with neighbours

            # if mid is first element in array
            if mid == 0 and nums[mid] > nums[mid + 1]:
                return mid

            # if mid is last element in array
            if mid == len(nums) - 1 and nums[mid] > nums[mid - 1]:
                return mid

            # if mid is any other in-between element in array
            if nums[mid] > nums[mid - 1] and nums[mid] > nums[mid + 1]:
                return mid

            # # we will move our pointers to the side where we find higher element

            elif nums[mid] < nums[mid + 1]:
                start = mid + 1

            else:
                end = mid - 1

        return -1


# result = Solution().findPeakElement([1, 2, 3, 1])  # 2
# result = Solution().findPeakElement([1, 2, 1, 3, 5, 6, 4])  # 5
# result = Solution().findPeakElement([1])  # 0
result = Solution().findPeakElement([3, 2, 1])  # 0
print(result)
