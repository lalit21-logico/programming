# *****************LCS************
# lcs subsequence
# lcSubString
# lcsPrint
# shortestCommonSs
# stringConversion
# largestPalindromSs
# minDelPalindrom
# minInsertPalindrome
# printShortestCommonSs
# longestRepeatingSs
# sequencePatternMatching

def lcs(x, y, m, n):
    mat = [[-1 for i in range(n+1)]for i in range(m+1)]
    for i in range(m+1):
        for j in range(n+1):
            if i == 0 or j == 0:
                mat[i][j] = 0
            elif x[i-1] == y[j-1]:
                mat[i][j] = 1+mat[i-1][j-1]
            else:
                mat[i][j] = max(mat[i][j-1], mat[i-1][j])
    return mat[m][n]


# print(lcs("sss", "ssfs", 3, 4))

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


# print(lcSubString("sss", "ssfs", 3, 4))

def lcsPrint(x, y, m, n):
    mat = [[-1 for i in range(n+1)]for i in range(m+1)]
    result = ""
    for i in range(m+1):
        for j in range(n+1):
            if i == 0 or j == 0:
                mat[i][j] = 0
            elif x[i-1] == y[j-1]:
                mat[i][j] = 1+mat[i-1][j-1]
            else:
                mat[i][j] = max(mat[i][j-1], mat[i-1][j])

    i, j = m, n
    while i > 0 and j > 0:
        if x[i-1] == y[j-1]:
            result = x[i-1] + result
            j -= 1
            i -= 1
        else:
            if mat[i][j-1] > mat[i-1][j]:
                j -= 1
            else:
                i -= 1
    return result


# print(lcsPrint("AGGTAB", "GXTXAYB", 6, 7))

# calling lcs
def shortestCommonSs(x, y, m, n):
    return len(x)+len(y) - lcs(x, y, m, n)
#print(shortestCommonSs("sss", "ssfs", 3, 4))


# calling lcs
def stringConversion(x, y, m, n):
    lc = lcs(x, y, m, n)
    ins = len(x)-lc
    dels = len(y)-lc
    return ["del:", dels, "ins", ins]

#print(stringConversion("sss", "ssfs", 3, 4))


# calling lcs
def largestPalindromSs(x, m):
    return lcs(x, x[::-1], m, m)
# print(largestPalindromSs("agbcba", 6))

# calling lcs


def minDelPalindrom(x, m):
    return len(x) - lcs(x, x[::-1], m, m)

# print(minDelPalindrom("agbcba", 6))


def minInsertPalindrome(x, m):
    return len(x) - lcs(x, x[::-1], m, m)

# print(minInsertPalindrome("agbcba", 6))


def printShortestCommonSs(x, y, m, n):
    mat = [[-1 for i in range(n+1)]for i in range(m+1)]
    result = ""
    for i in range(m+1):
        for j in range(n+1):
            if i == 0 or j == 0:
                mat[i][j] = 0
            elif x[i-1] == y[j-1]:
                mat[i][j] = 1+mat[i-1][j-1]
            else:
                mat[i][j] = max(mat[i][j-1], mat[i-1][j])

    i, j = m, n
    while i > 0 and j > 0:
        if x[i-1] == y[j-1]:
            result = x[i-1] + result
            j -= 1
            i -= 1
        else:
            if mat[i][j-1] > mat[i-1][j]:
                result = y[j-1] + result
                j -= 1
            else:
                result = x[i-1] + result
                i -= 1
    while(i > 0):
        result = x[i-1] + result
        i -= 1
    while(j > 0):
        result = y[j-1] + result
        j -= 1
    return result


# print(printShortestCommonSs("ABCDAF", "ACBCF", 6, 5))

def longestRepeatingSs(x, y, m, n):
    mat = [[-1 for i in range(n+1)]for i in range(m+1)]
    for i in range(m+1):
        for j in range(n+1):
            if i == 0 or j == 0:
                mat[i][j] = 0
            elif x[i-1] == y[j-1] and i != j:  # lcs to change here
                mat[i][j] = 1+mat[i-1][j-1]
            else:
                mat[i][j] = max(mat[i][j-1], mat[i-1][j])
    return mat[m][n]


# x = "aacbbsdd"
# print(longestRepeatingSs(x, x, 8, 8))

# calling lcs
def sequencePatternMatching(x, y, m, n):
    lc = lcs(x, y, m, n)
    if lc == len(x) or lc == len(y):
        return True
    else:
        return False


# print(sequencePatternMatching("sss", "ssfs", 3, 4))
