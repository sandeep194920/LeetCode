from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        combinations = []

        def parenthesis(open_p=0, close_p=0, brackets=''):

            if open_p == 0 & open_p < n:
                # arr.append('(')
                brackets = brackets + '('
                open_p += 1
            if open_p > close_p:
                if open_p < n:
                    parenthesis(open_p + 1, close_p, (brackets + '('))
                    parenthesis(open_p, close_p + 1, (brackets + ')'))
                else:
                    parenthesis(open_p, close_p + 1, (brackets + ')'))

            elif open_p == close_p:
                if open_p < n:
                    parenthesis(open_p + 1, close_p, (brackets + '('))
                else:
                    # base case open_p == close_p == n
                    combinations.append(brackets)

        parenthesis()

        return combinations


result = Solution().generateParenthesis(1)
print(result)
