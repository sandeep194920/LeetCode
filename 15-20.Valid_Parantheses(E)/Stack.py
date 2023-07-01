"""
Example 1:

Input: s = "()"
Output: true

Example 2:

Input: s = "()[]{}"
Output: true

Example 3:

Input: s = "(]"
Output: false

"""


# We will use stack(using array) to solve this problem

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {
            '(': ')',
            '[': ']',
            '{': '}',
        }

        for char in s:
            if len(stack) == 0:
                stack.append(char)
            else:
                top_el = stack[-1]
                if pairs.get(top_el) == char:
                    stack.pop()
                else:
                    stack.append(char)

        return len(stack) == 0


result = Solution().isValid("([)]")
# result = Solution().isValid("()[]{}")
# result = Solution().isValid("()[]{}")
# result = Solution().isValid("()[]{}")
# result = Solution().isValid("()[]{}")
print(result)
