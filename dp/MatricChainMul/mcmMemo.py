import sys

mat = [[-1 for i in range(101)] for i in range(101)]


def mcmMemo(array, i, j):
    if i >= j:
        return 0
    if mat[i][j] != -1:
        return mat[i][j]
    ans = sys.maxsize
    for k in range(i, j):
        temp_ans = mcmMemo(array, i, k) + mcmMemo(array, k+1,
                                                  j)+(array[i-1]*array[k]*array[j])
        ans = min(ans, temp_ans)
    mat[i][j] = ans
    return mat[i][j]


array = [10, 20, 30, 40, 30]
i = 1
j = len(array)
print(mcmMemo(array, i, j-1))
