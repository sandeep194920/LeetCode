def printFirstNegativeInteger(A, N, K):
    result = []
    for i in range(N-K+1): # 5 - 2  = 3 => i runs till index 3

        found = False

        for j in range(i, i+K): # j runs till index i + K
            if not found and A[j] < 0:
                found = True
                result.append(A[j])
                break

        if not found:
            result.append(0)

    return result


arr = [-8, 2, 3, -6, 10]
n = 5
k = 2
result = printFirstNegativeInteger(arr, n, k)
print(result)
