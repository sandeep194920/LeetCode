import math
from typing import List


def search_infinite_arr(nums: List[int], target: int) -> int:
    start, end = 0, 1
    while nums[end] <= target:
        start = end
        end = end * 2

    while start <= end:
        if nums[end] == target:
            return end
        mid = math.floor(start + (end - start) / 2)
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            end = mid - 1
        else:
            start = mid + 1

    return -1


# let's pretend that the input array given is infinite
result = search_infinite_arr([10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120], 60)
print(result)
