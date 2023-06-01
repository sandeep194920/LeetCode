"""
Efficient solution - Similar to TwoArraysTwoPasses but we use Single output array making space as only O(1)
"""


def product_except_self(nums):
    output = [1] * len(nums)
    left_product = right_product = 1

    # left to right traverse
    for i in range(1, len(nums)):  # this is same as for i in range(1, len(nums), 1):
        output[i] = left_product * nums[i - 1]
        left_product *= nums[i - 1]

#     At this point the output will be
#     [1, 1, 2, 6]
    for j in range(len(nums) - 1, -1, -1):
        output[j] = output[j] * right_product
        right_product *= nums[j]

#    At this point the output will be
#    [24, 12, 8, 6]
    return output


print(product_except_self([1, 2, 3, 4]))
