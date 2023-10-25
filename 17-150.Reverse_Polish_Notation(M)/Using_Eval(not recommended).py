# Using eval can be dangerous so we need to avoid that
from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = ['+', '-', '*', '/']
        for element in tokens:
            if element not in operators:
                stack.append(element)
            else:
                second_operand = stack.pop()
                first_operand = stack.pop()
                res = eval(f'{first_operand}{element}{second_operand}')
                stack.append(int(res))
        return stack[0]


# result = Solution().evalRPN(["2", "1", "+", "3", "*"])
# result = Solution().evalRPN(["4", "13", "5", "/", "+"])
result = Solution().evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"])
print(result)
