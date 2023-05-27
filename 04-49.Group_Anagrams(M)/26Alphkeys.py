"""
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
"""
from collections import defaultdict


def group_anagrams(strs):
    # storage = {}
    storage = defaultdict(list) # but make sure you return list of storage at the end
    for word in strs:
        unique_key = [0] * 26
        for c in word:
            unique_key[ord(c) - ord("a")] += 1

        # if tuple(unique_key) in storage:
        #     storage[tuple(unique_key)].append(word)
        # else:
        #     storage[tuple(unique_key)] = []

        # INFO: The above lines can be replaced by this below single line if defaultdict is used. defaultdict gives
        # us a list out of the box if storage[unique_key] doesn't exist, hence storage[unique_key] = [] is redundant
        storage[tuple(unique_key)].append(word)

    return list(storage.values())


print(group_anagrams(['eat', 'tea', 'tan', 'ate', 'nat', 'bat']))
