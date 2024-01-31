import math
from typing import List


def search_1_infinite_arr(nums: List[int]) -> int:
    start, end = 0, 1
    first_occ = -1
    while nums[end] < 1:
        start = end
        end = end * 2

    while start <= end:
        mid = math.floor(start + (end - start) / 2)
        if nums[mid] == 1:
            first_occ = mid
            end = end - 1
        elif nums[mid] < 1:
            start = mid + 1
        else:
            end = mid - 1

    return first_occ


result = search_1_infinite_arr([0, 0, 1, 1, 1, 1, 1, 1, 1])  # output = 2
# result = search_1_infinite_arr([1, 1, 1, 1, 1, 1]) # output = 0
print(result)
