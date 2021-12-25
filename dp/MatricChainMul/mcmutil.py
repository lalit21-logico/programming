# *******************matrix chain multiplication*****************
# mcmMemo
# palindromePartition
# boolexp
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


# array = [10, 20, 30, 40, 30]
# i = 1
# j = len(array)
# print(mcmMemo(array, i, j-1))


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


# mat = [[-1 for i in range(101)] for i in range(101)]
# string = "abcdedfwsddeff"
# i = 0
# j = len(string)
# print(palindromePartition(string, i, j))


dict = {}


def boolexp(string, i, j, bool):
    if i > j:
        return False
    if i == j:
        if bool == True:
            if string[i] == "T":
                return True
            else:
                return False
        else:
            if string[i] == "F":
                return True
            else:
                return False

    ke = str(i)+" "+str(j)+" "+str(bool)
    if ke in dict:
        return dict[ke]

    temp_ans = 0
    for k in range(i+1, j, 2):
        lt = boolexp(string, i, k-1, True)
        lf = boolexp(string, i, k-1, False)
        rt = boolexp(string, k+1, j, True)
        rf = boolexp(string, k+1, j, False)
        if (string[k] == '&'):
            if (bool == True):
                temp_ans = temp_ans + lt * rt
            else:
                temp_ans = temp_ans + lt * rf + lf * rt + lf * rf
        elif (string[k] == '|'):
            if (bool == True):
                temp_ans = temp_ans + lt * rt + lt * rf + lf * rt
            else:
                temp_ans = temp_ans + lf * rf
        elif (string[k] == '^'):
            if (bool == True):
                temp_ans = temp_ans + lt * rf + lf * rt
            else:
                temp_ans = temp_ans + lt * rt + lf * rf

    dict[ke] = temp_ans
    return temp_ans


# string = "T^F|F"
# i = 0
# j = len(string)
# print(boolexp(string, i, j-1, True))
