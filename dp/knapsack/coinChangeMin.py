import sys


def coinChangeMin(array, sum):
    mat = [[-1 for x in range(sum + 1)] for x in range(len(array) + 1)]
    for i in range(0, len(array) + 1):
        for j in range(0, sum + 1):

            if i == 0:
                mat[i][j] = 0
            elif j == 0:
                mat[i][j] = sys.maxsize - 1
            elif i == 1:
                if j % array[0] == 0:
                    mat[i][j] = j//array[0]
                else:
                    mat[i][j] = sys.maxsize - 1
            elif array[i-1] <= j:
                mat[i][j] = min(mat[i][j-array[i-1]] + 1, mat[i-1][j])
            else:
                mat[i][j] = mat[i-1][j]
    return mat[len(array)][sum]


sum = 11
array = [9, 6, 5, 1]
print(coinChangeMin(array, sum))
