def printFirstNegativeInteger(A, N, K):

    i, j = 0, 0
    negative_store = []
    window_negatives = []

    while j < N:

        if A[j] < 0:
            negative_store.append(A[j])

        if j - i + 1 < K:
            j += 1

        elif j - i + 1 == K:
            if len(negative_store) == 0:
                window_negatives.append(0)
            else:
                window_negatives.append(negative_store[0])
                if negative_store[0] == A[i]:
                    negative_store.pop(0)
            i += 1
            j += 1

    return window_negatives


arr = [-8, 2, 3, -6, 10]
n = 5
k = 2
result = printFirstNegativeInteger(arr, n, k)
print(result)
