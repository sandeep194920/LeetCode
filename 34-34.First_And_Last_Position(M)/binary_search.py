import math
from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def find_occurrence(occurrence='first'):
            fist_occurrence, last_occurrence = -1, -1
            start, end = 0, len(nums) - 1
            while start <= end:
                mid = math.floor(start + (end - start) / 2)
                if nums[mid] > target:
                    end = mid - 1
                elif nums[mid] < target:
                    start = mid + 1
                else:
                    if occurrence == 'first':
                        fist_occurrence = mid
                        end = mid - 1
                    else:
                        last_occurrence = mid
                        start = mid + 1
            if occurrence == 'first':
                return fist_occurrence
            else:
                return last_occurrence

        return [find_occurrence('first'), find_occurrence('last')]


# result = Solution().searchRange([5, 7, 7, 8, 8, 10], target=8) #  output [3, 4]
# result = Solution().searchRange([5, 7, 7, 8, 8, 10], target=6) #  output [-1, -1]
result = Solution().searchRange([], target=0)  # output [-1, -1]
print(result)
