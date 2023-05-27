"""
Input: nums = [1,2,3,1]
Output: true
"""


def contains_duplicates(nums):
    unique_elements = set()
    for num in nums:
        if num in unique_elements:
            return True
        unique_elements.add(num)
    return False


result = contains_duplicates([1, 2, 3])
print(result)
