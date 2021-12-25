
mat = [[-1]*100]*100


def knap(weight, value, w, n):
    if w == 0 or n == 0:
        return 0
    if mat[n][w] != -1:
        return mat[n][w]
    if weight[n-1] <= w:
        mat[n][w] = max(value[n-1]+knap(weight, value, w-weight[n-1], n-1),
                        knap(weight, value, w, n-1))
        return mat[n][w]

    elif weight[n-1] > w:
        mat[n][w] = knap(weight, value, w, n-1)
        return mat[n][w]


w = 50
value = [60, 100, 120]
weight = [10, 20, 30]
n = len(value)
maximum = knap(weight, value, w, n)
print(maximum)
# print(mat)
