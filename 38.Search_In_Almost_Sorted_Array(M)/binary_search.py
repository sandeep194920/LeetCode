import math
from typing import List


class Solution:
    def find_element(self, nums: List[int], key: int) -> int:
        start, end = 0, len(nums) - 1
        while start <= end:
            mid = math.floor(start + (end - start) / 2)
            if nums[mid] == key:
                return mid
            # along with mid. we also check for mid's neighbours
            elif mid - 1 >= 0 and nums[mid - 1] == key:
                return mid - 1
            elif mid + 1 <= len(nums) - 1 and nums[mid + 1] == key:
                return mid + 1

            # now we move end and start (we don't have to move to mid -1 or mid + 1
            # as we already would have checked that)
            elif nums[mid] < key:
                start = mid + 2
            else:
                end = mid - 2

        return -1


result = Solution().find_element([10, 3, 40, 20, 50, 80, 70], 90)
print(result)
