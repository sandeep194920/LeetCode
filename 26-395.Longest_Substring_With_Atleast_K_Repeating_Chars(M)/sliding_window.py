class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        i, j = 0, 0
        maximum, count = 0, 0
        frequency = {}

        while j < len(s):

            frequency[s[j]] = frequency.get(s[j], 0) + 1

            if frequency[s[j]] == 1:
                count += 1

            if count < k:
                j += 1

            elif count == k:
                maximum = max(maximum, j - i + 1)
                j += 1

            # if count>k in the below else block
            else:
                removable_char = s[i]
                while frequency[removable_char] > 0:
                    if s[i] == removable_char:
                        frequency[removable_char] -= 1
                        if frequency[removable_char] == 0:
                            count -= 1
                    i += 1
                j += 1

        return maximum


result = Solution().longestSubstring(s="aaabb", k=3)
print(result)

