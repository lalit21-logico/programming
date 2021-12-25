def lcSubString(x, y, m, n):
    mat = [[-1 for i in range(n+1)]for i in range(m+1)]
    result = 0
    for i in range(m+1):
        for j in range(n+1):
            if i == 0 or j == 0:
                mat[i][j] = 0
            elif x[i-1] == y[j-1]:
                mat[i][j] = 1+mat[i-1][j-1]
                result = max(result, mat[i][j])
            else:
                mat[i][j] = 0
    return result


print(lcSubString("sss", "ssfs", 3, 4))
