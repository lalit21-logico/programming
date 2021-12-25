import sys


def palindromePartition(string, i, j):
    if i >= j:
        return 0
    if string[i:j+1] == string[i:j+1][::-1]:
        return 0
    if mat[i][j] != -1:
        return mat[i][j]
    ans = sys.maxsize
    for k in range(i, j):

        if mat[i][k] != -1:
            left = mat[i][k]
        else:
            left = palindromePartition(string, i, k)
            mat[i][k] = left

        if mat[k+1][j] != -1:
            right = mat[k+1][j]
        else:
            right = palindromePartition(string, k+1, j)
            mat[k+1][j] = right
        temp = left + right + 1
        ans = min(ans, temp)
    mat[i][j] = ans
    return ans


mat = [[-1 for i in range(101)] for i in range(101)]
string = "abcdedfwsddeff"
i = 0
j = len(string)
print(palindromePartition(string, i, j))
