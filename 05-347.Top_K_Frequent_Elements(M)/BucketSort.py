"""
Approach - Present in the README as well, but briefly explained here

Say you have [d,d,d,d] -> You will use a hashmap first to track number of times d has occurred -> {d:4}

Then the key part is, you need to layout placeholders (length will be same as input length)
Meaning, if you have dddd, then you need 5 placeholders _ _ _ _ _

Loop over length of input and then look at hashmap and then fill the array this way

                d
_   _   _   _   _
0   1   2   3   4
"""


def top_k_frequent_elements(nums, k):
    frequencies = {}
    for num in nums:
        frequencies[num] = 1 + frequencies.get(num, 0)

    # At this point the frequencies will be
    # {
    #     1 : 3,
    #     2 : 2,
    #     3 : 1
    # }

    result_arr = [[] for i in range(len(nums) + 1)]
    for key, val in frequencies.items():
        result_arr[val].append(key)
    print(result_arr)

    k_elements = []
    for i in range(len(result_arr) - 1, 0, -1):
        for el in result_arr[i]:
            k_elements.append(el)
            if len(k_elements) == k:
                return k_elements


# result = top_k_frequent_elements([1, 1, 1, 2, 2, 3], 2)
# result = top_k_frequent_elements([1, 2], 2)
result = top_k_frequent_elements([1], 1)
print(result)
