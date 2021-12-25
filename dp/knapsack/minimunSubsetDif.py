def minimunSubsetDif(array, sum):
    mat = [[-1 for x in range(sum + 1)] for x in range(len(array) + 1)]
    for i in range(0, len(array) + 1):
        for j in range(0, sum + 1):
            if j == 0:
                mat[i][j] = True
            elif i == 0:
                mat[i][j] = False
            elif array[i-1] <= j:
                mat[i][j] = mat[i-1][j-array[i-1]] or mat[i-1][j]
            else:
                mat[i][j] = mat[i-1][j]
    mn = sum
    for i in range(0, sum//2+1):
        if mat[len(array)][i] == True:
            mn = min(mn, sum-(2*i))
    return mn


array = [1, 2, 7]
print(minimunSubsetDif(array, sum(array)))
