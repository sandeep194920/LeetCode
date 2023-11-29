class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # t_map is to quickly get the elements of t in O(1) lookup
        t_map = {}
        for ch in t:
            t_map[ch] = t_map.get(ch, 0) + 1

        i, j, count = 0, 0, len(t_map)  # count is basically to track when an element in t_map becomes 0 or 1
        current_str = ''
        min_str = ''

        while j < len(s):
            current_str = current_str + s[j]
            if s[j] in t_map:
                t_map[s[j]] -= 1
                if t_map[s[j]] == 0:
                    count -= 1

            if count > 0:
                j += 1

            elif count == 0:
                while count == 0:
                    if len(current_str) < len(min_str) or min_str == '':
                        min_str = current_str
                    if s[i] in t_map:
                        t_map[s[i]] += 1
                        if t_map[s[i]] == 1:
                            count += 1
                    current_str = current_str[1:]
                    i += 1
                j += 1

        return min_str


result = Solution().minWindow(s="ADOBECODEBANC", t="ABC")
# result = Solution().minWindow(s="a", t="aa")
# result = Solution().minWindow(s="aa", t="aa")
print(result)
