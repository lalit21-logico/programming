# util indexing
# ******************knapsack*********************
# knapsack
# subsetSum
# equalSumPartition
# countSubsetSum
# minimunSubsetDif
# minimunSubsetDif
# target sum +/- assign wala

# ******************************#unbounded knapsack*************
# unbounded Knapsack / rod cutting same
# coin change max
# coin change min

import sys

# start knapsack


def knapsack(weight, value, w, n):
    mat = [[-1 for x in range(w + 1)] for x in range(n + 1)]
    for i in range(0, n + 1):
        for j in range(0, w + 1):
            if i == 0 or j == 0:
                mat[i][j] = 0
            elif weight[i-1] <= w:
                mat[i][j] = max(value[i-1] + mat[i-1]
                                [j-weight[i-1]], mat[i-1][j])
            else:
                mat[i][j] = mat[i-1][j]

    return mat[n][w]


# w = 50
# value = [60, 100, 120]
# weight = [10, 20, 30]
# n = len(value)
# maximum = knapsack(weight, value, w, n)
# print(maximum)


def subsetSum(array, sum_a):
    mat = [[-1 for x in range(sum_a + 1)] for x in range(len(array) + 1)]
    for i in range(0, len(array) + 1):
        for j in range(0, sum_a + 1):
            if j == 0:
                mat[i][j] = True
            elif i == 0:
                mat[i][j] = False
            elif array[i-1] <= j:
                mat[i][j] = mat[i-1][j-array[i-1]] or mat[i-1][j]
            else:
                mat[i][j] = mat[i-1][j]
    return mat[len(array)][sum_a]


# sum_a = 10
# array = [2, 4, 6, 4, 3]
# print(subsetSum(array, sum_a))

# also call subsetSum


def equalSumPartition(array, sum_a):
    if sum(array) % 2 != 0:
        return False
    else:
        return subsetSum(array, sum_a//2)


# sum_a = 10
# array = [2, 4, 6, 4, 4]
# print(equalSumPartition(array, sum_a))

#  count subset sum


def countSubsetSum(array, sum_a):
    mat = [[-1 for x in range(sum_a + 1)] for x in range(len(array) + 1)]
    for i in range(0, len(array) + 1):
        for j in range(0, sum_a + 1):
            if j == 0:
                mat[i][j] = 1
            elif i == 0:
                mat[i][j] = 0
            elif array[i-1] <= j:
                mat[i][j] = mat[i-1][j-array[i-1]] + mat[i-1][j]
            else:
                mat[i][j] = mat[i-1][j]
    return mat[len(array)][sum_a]


# sum_a = 10
# array = [2, 4, 6, 4, 3]
# print(countSubsetSum(array, sum_a))


def minimunSubsetDif(array, sum_a):
    mat = [[-1 for x in range(sum_a + 1)] for x in range(len(array) + 1)]
    for i in range(0, len(array) + 1):
        for j in range(0, sum_a + 1):
            if j == 0:
                mat[i][j] = True
            elif i == 0:
                mat[i][j] = False
            elif array[i-1] <= j:
                mat[i][j] = mat[i-1][j-array[i-1]] or mat[i-1][j]
            else:
                mat[i][j] = mat[i-1][j]
    mn = sum_a
    for i in range(0, sum_a//2+1):
        if mat[len(array)][i] == True:
            mn = min(mn, sum_a-(2*i))
    return mn


# array = [1, 2, 7]
# print(minimunSubsetDif(array, sum(array)))

# calling  countSubsetSum


def countSubsetDif(array, dif):
    sum_a = (sum(array)+dif)//2
    return countSubsetSum(array, sum_a)


# array = [1, 1, 2, 3]
# dif = 1
# print(countSubsetDif(array, dif))

# calling  countSubsetSum
def targetSum(array, dif):
    sum_a = (sum(array)+dif)//2
    return countSubsetSum(array, sum_a)


# array = [1, 1, 2, 3]
# sum_a = 1
# print(targetSum(array, sum_a))


# unboundedknapsack
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


# w = 50
# value = [60, 100, 120]
# weight = [10, 20, 30]
# n = len(value)
# maximum = unboundedKnapsack(weight, value, w, n)
# print(maximum)

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


# sum = 10
# array = [2, 4, 6, 4, 3]
# print(coinChangeMax(array, sum))


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


# sum = 11
# array = [9, 6, 5, 1]
# print(coinChangeMin(array, sum))
