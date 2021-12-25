
def unboundedKnapsack(weight, value, w, n):
    mat = [[-1 for x in range(w + 1)] for x in range(n + 1)]
    for i in range(0, n + 1):
        for j in range(0, w + 1):
            if i == 0 or j == 0:
                mat[i][j] = 0
            elif weight[i-1] <= w:
                mat[i][j] = max(value[i-1] + mat[i]
                                [j-weight[i-1]], mat[i-1][j])
            else:
                mat[i][j] = mat[i-1][j]

    return mat[n][w]


w = 50
value = [60, 100, 120]
weight = [10, 20, 30]
n = len(value)
maximum = unboundedKnapsack(weight, value, w, n)
print(maximum)
# print(mat)
