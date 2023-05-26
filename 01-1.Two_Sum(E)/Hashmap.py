def two_sum(nums, target):
    cache = {}  # {number : index}
    for i, num in enumerate(nums):
        key = target - num
        if key in cache:
            return cache[key], i
        cache[num] = i


print(two_sum([2, 7, 11, 15], 9))
