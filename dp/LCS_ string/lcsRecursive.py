def lcsRec(x, y, m, n):
    if m == 0 or n == 0:
        return 0
    if x[m-1] == y[n-1]:
        return 1 + lcsRec(x, y, m-1, n-1)
    else:
        return max(lcsRec(x, y, m, n-1), lcsRec(x, y, m-1, n))


print(lcsRec("sss", "ssfs", 3, 4))
