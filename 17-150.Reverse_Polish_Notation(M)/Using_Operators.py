# Using eval can be dangerous so we need to avoid that
from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for element in tokens:
            if element == '+':

                stack.append(stack.pop() + stack.pop())
            elif element == '-':
                second_operand = stack.pop()
                first_operand = stack.pop()
                stack.append(second_operand - first_operand)
            elif element == '*':
                first_operand, second_operand = stack.pop(), stack.pop()
                stack.append(second_operand * first_operand)
            elif element == '/':
                first_operand, second_operand = stack.pop(), stack.pop()
                stack.append(int(second_operand/first_operand))
            else:
                stack.append(int(element))

        return stack[0]


# result = Solution().evalRPN(["2", "1", "+", "3", "*"])
# result = Solution().evalRPN(["4", "13", "5", "/", "+"])
result = Solution().evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"])
print(result)
