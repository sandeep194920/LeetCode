import math

import math
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def get_mid_point():
            start, end = 0, len(nums) - 1
            while start <= end:
                mid = math.floor(start + (end - start) / 2)

                next_index = (mid + 1) % len(nums)
                prev_index = (mid - 1 + len(nums)) % len(nums)

                if nums[prev_index] > nums[mid] and nums[mid] < nums[next_index]:
                    return mid
                elif nums[mid] > nums[end]:
                    start = mid + 1
                else:
                    end = mid - 1
            # if there is 1 element in the array, while loop is not executed, so we need to return here
            # note that, as per the constraints, we can't have 0 elements in array
            return nums[0]

        def bin_search(start, end):
            while start <= end:
                mid = math.floor(start + (end - start) / 2)
                if nums[mid] == target:
                    return mid
                elif nums[mid] > target:
                    end = mid - 1
                else:
                    start = mid + 1
            return -1

        before_mid = bin_search(0, get_mid_point() - 1)
        after_mid = bin_search(get_mid_point(), len(nums) - 1)
        return max(before_mid, after_mid)


# result = Solution().search([4, 5, 6, 7, 0, 1, 2], target=0)  # output 4
# result = Solution().search([4, 5, 6, 7, 0, 1, 2], target=3)  # output -1
result = Solution().search([1], target=0)  # output -1
# result = Solution().search([1, 3], target=3)  # output -1
print(result)
