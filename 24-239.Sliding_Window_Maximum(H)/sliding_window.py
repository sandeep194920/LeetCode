"""
Not doing a bruteforce code for this as it is similar to first 2 problems 21 and 22.
We will come back and code if necessary
"""
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        i, j = 0, 0
        max_window_elements = []
        store = []  # the first element of this list should always be the larger one.
        # It can have smaller elements to right of it.
        # If there is ever a larger element that has to be added,
        # then all smaller elements to it's left should be popped

        while j < len(nums):

            # 'calculation' part
            if len(store) == 0:
                store.append(nums[j])
            elif nums[j] >= store[-1]:
                store = [nums[j]]  # popping all elements of this store and adding this biggest element to the start
            else:
                store.append(nums[j])  # this list can have same numbers like [3, 3]

            # 'checking window size' part
            if j - i + 1 < k:
                j += 1

            # 'window size becomes same' part
            elif j - i + 1 == k:
                # now that window size is k, we first note the highest element of this window
                max_window_elements.append(store[0])

                # we need to first check if first element in store is a[i],
                # and remove that if same before we slide the window
                if nums[i] == store[0]:
                    store.pop(0)
                i += 1
                j += 1

        return max_window_elements


# result = Solution().maxSlidingWindow(nums=[1, 3, -1, -3, 5, 3, 6, 7], k=3)
#
# print(result)  # [3,3,5,5,6,7]


# result = Solution().maxSlidingWindow(nums=[1, -1], k=1)
#
# print(result)  # [1, -1]


# result = Solution().maxSlidingWindow(nums=[9, 11], k=2)
#
# print(result)  # [11]


result = Solution().maxSlidingWindow(nums=[1, 3, 1, 2, 0, 5], k=3)

print(result)  # [3,3,2,5]
