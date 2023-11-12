"""
You get Time Limit Exceeded error for large input
"""
from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        output = [0 for _ in temperatures]

        for i in range(len(temperatures)):
            days = 1  # 1 to begin with because i and j is 1 day difference when we start
            for j in range(i+1, len(temperatures)):
                if temperatures[j] > temperatures[i]:
                    output[i] = days
                    break
                else:
                    days += 1

        return output


temps = [73, 74, 75, 71, 69, 72, 76, 73]
result = Solution().dailyTemperatures(temps)
print(result)
