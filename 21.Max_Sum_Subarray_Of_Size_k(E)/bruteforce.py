class Solution:
    def maximumSumSubarray(self, K, Arr, N):
        max_sum = 0
        for i in range(N-K+1):
            total = 0
            for j in range(i, i+K):
                total = total + Arr[j]
            max_sum = max(max_sum, total)
        return max_sum


N = 4
K = 3
Arr = [100, 200, 300, 400]
maxSum = Solution().maximumSumSubarray(K, Arr, N)
print(maxSum)
