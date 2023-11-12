"""
this is similar to previous problem Next_Greater_Element (step 2). But we need to store number + index of that
number in the stack and find the difference between indices before putting element on to top of stack with current
top of stack
"""
from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        m_stack = [(temperatures[-1], len(temperatures)-1)]
        output = [0]
        for i in range(len(temperatures)-2, -1, -1):

            current = temperatures[i]

            # if current element is less than tos
            # get tos index and subtract that from current i and add that to output
            # add current to stack with index

            if current < m_stack[-1][0]:
                output.insert(0, m_stack[-1][1] - i)
                m_stack.append((current, i))
                continue

            # else if current is greater than tos, then we need to pop stack until we find tos more than current
            # or until we find no elements to add a 0 to o/p array

            while len(m_stack) != 0:
                if m_stack[-1][0] <= current:
                    m_stack.pop()
                else:
                    output.insert(0, m_stack[-1][1] - i)
                    m_stack.append((current, i))
                    break
            else:
                output.insert(0, 0)
                m_stack.append((current, i))

        return output


temps = [73, 74, 75, 71, 69, 72, 76, 73]
result = Solution().dailyTemperatures(temps)
print(result)
