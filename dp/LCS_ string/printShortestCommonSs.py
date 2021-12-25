def printShortestCommonSs(x, y, m, n):
    mat = [[-1 for i in range(n+1)]for i in range(m+1)]
    result = ""
    for i in range(m+1):
        for j in range(n+1):
            if i == 0 or j == 0:
                mat[i][j] = 0
            elif x[i-1] == y[j-1]:
                mat[i][j] = 1+mat[i-1][j-1]
            else:
                mat[i][j] = max(mat[i][j-1], mat[i-1][j])

    i, j = m, n
    while i > 0 and j > 0:
        if x[i-1] == y[j-1]:
            result = x[i-1] + result
            j -= 1
            i -= 1
        else:
            if mat[i][j-1] > mat[i-1][j]:
                result = y[j-1] + result
                j -= 1
            else:
                result = x[i-1] + result
                i -= 1
    while(i > 0):
        result = x[i-1] + result
        i -= 1
    while(j > 0):
        result = y[j-1] + result
        j -= 1
    return result


print(printShortestCommonSs("ABCDAF", "ACBCF", 6, 5))
