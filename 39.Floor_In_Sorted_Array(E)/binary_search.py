import math
from typing import List


def floor_search(nums: List[int], target: int) -> int:
    start, end = 0, len(nums) - 1
    output = -1
    while start <= end:

        if nums[end] <= target:
            return nums[end]

        mid = math.floor(start + (end - start) / 2)

        if nums[mid] == target:
            return nums[mid]

        elif nums[mid] > target:
            end = mid - 1

        else:
            # nums[mid] is less than the target so it could be a candidate, hence we will store that in output first
            output = nums[mid]
            start = mid + 1

    return output


result = floor_search([1, 2, 8, 10, 10, 12, 19], 5)  # output 2
# result = floor_search([1, 2, 8, 10, 10, 12, 19], 20)  # output 19
# result = floor_search([1, 2, 8, 10, 10, 12, 19], 0)  # output -1
print(result)
