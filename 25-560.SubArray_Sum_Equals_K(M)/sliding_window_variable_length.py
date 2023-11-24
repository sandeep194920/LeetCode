# This solution won't work for negative numbers as explained in readme and below.

# https://www.geeksforgeeks.org/longest-sub-array-sum-k/

from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        i, j = 0, 0
        total = 0
        number_of_sub_arrays = 0
        while j < len(nums):
            # calculations
            total += nums[j]

            if total < k:
                j += 1

            elif total == k:
                # update the result array
                number_of_sub_arrays += 1
                j += 1

            else:
                # remove calculation for i and increment i
                while total > k:
                    total -= nums[i]
                    i += 1
                    if total == k and i <= j:
                        number_of_sub_arrays += 1
                j += 1

        return number_of_sub_arrays


# result = Solution().subarraySum(nums=[1, 1, 1], k=2)
# result = Solution().subarraySum(nums=[1, 2, 3], k=3)
result = Solution().subarraySum(nums=[1], k=0)

print(result)
