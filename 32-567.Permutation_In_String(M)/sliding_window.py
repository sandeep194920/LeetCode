class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        i, j = 0, 0
        occurances_map = {}

        for ch in s1:
            occurances_map[ch] = occurances_map.get(ch, 0) + 1
        count = len(occurances_map)

        while j < len(s2):
            if s2[j] in occurances_map:
                occurances_map[s2[j]] -= 1
                if occurances_map[s2[j]] == 0:
                    count -= 1
                    if count == 0:
                        return True

                elif occurances_map[s2[j]] < 0:
                    while occurances_map[s2[j]] != 0:
                        if s2[i] in occurances_map:
                            occurances_map[s2[i]] += 1
                            if occurances_map[s2[i]] == 1:
                                count += 1
                        i += 1
            else:
                j += 1
                while i != j:
                    if s2[i] in occurances_map:
                        occurances_map[s2[i]] += 1
                        if occurances_map[s2[i]] == 1:
                            count += 1

                    i += 1

                continue

            j += 1

        return False


# result = Solution().checkInclusion(s1="ab", s2="eidbaooo")  # true
# result = Solution().checkInclusion(s1="ab", s2="eidboaoo")  # false
# MY FAILED CASES
result = Solution().checkInclusion(s1="hello", s2="ooolleoooleh")  # false
# result = Solution().checkInclusion(s1="adc", s2="dcda")  # true

print(result)

"""
{
d: 1 0 -1
c: 1 0 
a: 1
}
"""
