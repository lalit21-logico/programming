def subsetSum(array, sum):
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
    return mat[len(array)][sum]


def equalSumPartition(array, sum_a):
    if sum(array) % 2 != 0:
        return False
    else:
        return subsetSum(array, sum_a//2)


sum_a = 12
array = [2, 4, 6, 4, 4]
print(equalSumPartition(array, sum_a))
