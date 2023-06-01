"""
TwoPass approach -> !st pass from left to right, and next pass from right to left
Input: nums = [1,2,3,4]
Output: [24,12,8,6]
"""


#   P = 1           [1      2       3      4]    P = 24
#   Left to right   [1      1       2      6]
#   Right to left   [24     12      4      1]
#   output = Left to right *  Right to left


def product_except_self(nums):
    left_arr,  right_arr = [1] * len(nums), [1] * len(nums)

    product_until_element = 1

    # left to right pass
    for i in range(1, len(nums), 1):
        left_arr[i] = product_until_element * nums[i - 1]
        product_until_element *= nums[i - 1]

    # right to left pass
    product_until_element = 1

    for j in range(len(nums) - 2, -1, -1):
        right_arr[j] = product_until_element * nums[j + 1]
        product_until_element *= nums[j + 1]

    output = []
    for k in range(len(nums)):
        output.append(left_arr[k] * right_arr[k])

    return output


print(product_except_self([1, 2, 3, 4]))
