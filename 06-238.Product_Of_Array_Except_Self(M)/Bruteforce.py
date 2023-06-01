"""
Input: nums = [1,2,3,4]
Output: [24,12,8,6]
"""


def product_except_self(nums):
    output = [1] * len(nums)
    for i in range(len(nums)):
        product = 1
        for j in range(0, i, 1):
            product *= nums[j]

        for k in range(i + 1, len(nums), 1):
            product *= nums[k]

        output[i] = product
    return output


print(product_except_self([1, 2, 3, 4]))
