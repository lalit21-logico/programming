def coinChangeMax(array, sum):
    mat = [[-1 for x in range(sum + 1)] for x in range(len(array) + 1)]
    for i in range(0, len(array) + 1):
        for j in range(0, sum + 1):
            if j == 0:
                mat[i][j] = 1
            elif i == 0:
                mat[i][j] = 0
            elif array[i-1] <= j:
                mat[i][j] = mat[i][j-array[i-1]] + mat[i-1][j]
            else:
                mat[i][j] = mat[i-1][j]

    return mat[len(array)][sum]


sum = 17
array = [3, 4, 6, 4, 2]
print(coinChangeMax(array, sum))
