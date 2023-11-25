# This is a good technique as it is similar to previous problem
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i, j = 0, 0
        maximum = 0  # No need to take count here as we just use length of frequency
        frequency = {}

        while j < len(s):
            frequency[s[j]] = frequency.get(s[j], 0) + 1

            # we will check if size of frequency is same as length of
            # window (j-i+1). If they are same that means we have all
            # unique characters until that point.
            # THIS IS THE LOGIC I HAD MISSED IN MY FIRST SOLUTION OF THIS PROBLEM
            if len(frequency) == j - i + 1:
                maximum = max(maximum, j - i + 1)
                j += 1

            # we will never hit len(frequency) > j-i+1 as length of window
            # will always be same size of frequency or more than frequency. Think about it!!
            elif len(frequency) < j - i + 1:
                # if this is the case then there is a repeating character
                while len(frequency) < j - i + 1 and j != i:
                    frequency[s[i]] -= 1
                    if frequency[s[i]] == 0:
                        del frequency[s[i]]
                    i += 1
                j += 1

        return maximum


result = Solution().lengthOfLongestSubstring(s="abcabcbb")  # 3
# result = Solution().lengthOfLongestSubstring(s="bbbbb")  # 1
# result = Solution().lengthOfLongestSubstring(s="pwwkew")  # 3
print(result)
