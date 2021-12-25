num_cases = int(input())
for case in range(1, num_cases + 1):
    num = int(input())
    for round in range(1, num + 1):
        coin_count = 0
        I, N, Q = input().split()
        I, N, Q = int(I), int(N), int(Q)
        if N % 2 == 0:
            print(N // 2)
        else:
            if I == Q:
                print(N // 2)
            else:
                print((N // 2)+1)
