
mat = [[-1 for x in range(100 + 1)] for x in range(100 + 1)]


def lcsRec(x, y, m, n):

    if m == 0 or n == 0:
        return 0
    if mat[m][n] != -1:
        return mat[m][n]
    if x[m-1] == y[n-1]:
        mat[m][n] = 1 + lcsRec(x, y, m-1, n-1)
        return mat[m][n]
    else:
        mat[m][n] = max(lcsRec(x, y, m, n-1), lcsRec(x, y, m-1, n))
        return mat[m][n]


print(lcsRec("sss", "ssfs", 3, 4))
