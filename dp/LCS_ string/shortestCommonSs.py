def lcs(x, y, m, n):
    mat = [[-1 for i in range(n+1)]for i in range(m+1)]
    for i in range(m+1):
        for j in range(n+1):
            if i == 0 or j == 0:
                mat[i][j] = 0
            elif x[i-1] == y[j-1]:
                mat[i][j] = 1+mat[i-1][j-1]
            else:
                mat[i][j] = max(mat[i][j-1], mat[i-1][j])
    return mat[m][n]

# calling lcs


def shortestCommonSs(x, y, m, n):
    return len(x)+len(y) - lcs(x, y, m, n)


print(shortestCommonSs("AGGTAB", "GXTXAYB", 6, 7))
