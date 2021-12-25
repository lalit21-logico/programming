import sys


def mcmRec(array, i, j):
    if i >= j:
        return 0
    ans = sys.maxsize
    for k in range(i, j):
        temp_ans = mcmRec(array, i, k) + mcmRec(array, k+1,
                                                j)+(array[i-1]*array[k]*array[j])
        ans = min(ans, temp_ans)
    return ans


array = [10, 20, 30, 40, 30]
i = 1
j = len(array)
print(mcmRec(array, i, j-1))
