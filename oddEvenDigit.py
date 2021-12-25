def getOddSum(num):
    result = 0
    i = 1
    while i < len(num):
        result = result + int(num[i])
        i = i+2
    return str(result)


def getEvenSum(num):
    result = 0
    i = 0
    while(i < len(num)):
        result = result + int(num[i])
        i = i+2
    return str(result)


def get_result(n, d):
    if int(n) < 10:
        if n == d:
            return True
        else:
            False
    else:
        return get_result(getEvenSum(n), d) or get_result(getOddSum(n), d)


t = int(input())
while t != 0:
    st = input().split()
    n = st[0]
    d = st[1]
    if get_result(n, d):
        print("YES")
    else:
        print("NO")
    t -= 1
