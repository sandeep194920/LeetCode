# The function in backtrack.py can be improved


from typing import List


class Solution:
    def generateParenthesis(self, n: int):

        combinations = []

        def parenthesis(open_p=0, close_p=0, brackets=''):

            # base case
            if open_p == close_p == n:
                combinations.append(brackets)

            if open_p < n:
                parenthesis(open_p + 1, close_p, (brackets + '('))
            if close_p < open_p:
                parenthesis(open_p, close_p + 1, (brackets + ')'))

        parenthesis()
        return combinations


result = Solution().generateParenthesis(3)
print(result)

