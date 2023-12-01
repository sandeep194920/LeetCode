class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        i, j = 0, 0
        max_count = 0
        frequency = {}

        def get_highest():
            highest = 0
            for ch in frequency:
                highest = max(highest, frequency[ch])
            return highest

        while j < len(s):
            frequency[s[j]] = frequency.get(s[j], 0) + 1
            high = get_highest()
            traversed = j - i + 1

            # You should update the max_count for every traverse even when k is less than k
            # otherwise it doesn't work for example, s = AAAA, k = 2
            # if traversed - high < k:
            #     j += 1

            if traversed - high <= k:
                max_count = max(max_count, j - i + 1)
                j += 1

            else:
                frequency[s[i]] -= 1
                i += 1
                j += 1

        return max_count


# result = Solution().characterReplacement(s="ABAB", k=2)  # output is 4
# result = Solution().characterReplacement(s="AABABBA", k=1)  # output is 4
# result = Solution().characterReplacement(s="ABABBA", k=2)  # output is 5
result = Solution().characterReplacement(s="AAAA", k=2)  # EDGE CASE - output is 4 and not 0
print(result)
