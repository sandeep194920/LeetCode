# BAD SOLUTION EVEN THOUGH SLIDING WINDOW (because it is similar to previous problem
# but I used a different approach. Always use similar approaches so you can solve easily)

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        i, j = 0, 0
        maximum, count = 0, 0
        frequency = {}

        while j < len(s):
            frequency[s[j]] = frequency.get(s[j], 0) + 1
            count += 1

            if frequency[s[j]] <= 1:
                j += 1

            else:
                maximum = max(maximum, count - 1)
                while s[i] != s[j]:
                    count -= 1
                    frequency[s[i]] -= 1
                    i += 1
                else:
                    count -= 1
                    frequency[s[i]] -= 1
                    i += 1
                    j += 1

        maximum = max(maximum, count)
        return maximum


# result = Solution().lengthOfLongestSubstring(s="abcabcbb")  # 3
# result = Solution().lengthOfLongestSubstring(s="bbbbb")  # 1
result = Solution().lengthOfLongestSubstring(s="pwwkew")  # 4
print(result)
