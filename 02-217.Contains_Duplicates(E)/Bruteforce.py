"""
Input: nums = [1,2,3,1]
Output: true
"""


def contains_duplicates(nums):
    for i in range(len(nums) - 1):
        for j in range(i+1, len(nums)):
            if nums[i] == nums[j]:
                return True
    return False


result = contains_duplicates([1, 2, 3, 4])
print(result)
