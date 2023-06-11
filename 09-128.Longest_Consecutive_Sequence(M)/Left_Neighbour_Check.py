# Input: nums = [100,4,200,1,3,2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.


def longest_consecutive(nums):
    longest_sequence = 0
    nums = set(nums)
    for num in nums:
        if num - 1 in nums:
            continue
        current_length = 1
        next_num = num + 1
        while next_num in nums:
            current_length += 1
            next_num += 1
        longest_sequence = max(longest_sequence, current_length)
    return longest_sequence


# result = longest_consecutive([100, 4, 200, 1, 3, 2])
result = longest_consecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1])
# result = longest_consecutive([]) # Edge case
# result = longest_consecutive([1]) # Edge case
# result = longest_consecutive([1, 1]) # Edge case
print(result)
