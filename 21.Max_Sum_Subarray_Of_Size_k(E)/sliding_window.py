class Solution:
    def maximumSumSubarray(self, K, Arr, N):
        i, j = 0, 0
        total, maximum = 0, 0
        while j < N:
            total += Arr[j]
            if j - i + 1 < K:
                j += 1
            elif j - i + 1 == K:
                maximum = max(total, maximum)
                total = total - Arr[i]
                i += 1
                j += 1
        return maximum


N = 4
K = 2
Arr = [100, 200, 300, 400]
maxSum = Solution().maximumSumSubarray(K, Arr, N)
print(maxSum)
