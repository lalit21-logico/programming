

num_cases = int(input())
for case in range(1, num_cases + 1):
    N = int(input())
    max_profit = 0
    for i in range(1, N + 1):
        s, p, v = input().split()
        if max_profit < (int(p)//(int(s)+1))*int(v):
            max_profit = int((int(p)//(int(s)+1))*int(v))

    print(max_profit)
