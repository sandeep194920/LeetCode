from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        i, j = 0, len(matrix[0]) - 1
        while i < len(matrix) and j >= 0:
            if matrix[i][j] == target:
                return True
            # elif i < len(matrix) - 1 and matrix[i + 1][j] > target or len(matrix) == 1:
            elif matrix[i][j] > target:
                j = j - 1
            else:
                i = i + 1
        return False


# result = Solution().searchMatrix(matrix=[[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], target=3)  # true
# result = Solution().searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], target=13)  # false
# result = Solution().searchMatrix([[1]], target=13)  # false
# result = Solution().searchMatrix([[1, 3]], target=1)  # true
result = Solution().searchMatrix([[1], [3]], target=1)  # true
print(result)
