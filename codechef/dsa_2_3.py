num_cases = int(input())
for case in range(1, num_cases + 1):
    N = int(input())
    boxes = list(map(int, input().split()))
    tokens = 0
    fill = 0
    while(1):
        small = 1000000
        temp = 0
        for i in range(0, N):
            print("i", i)
            if small >= boxes[i]:
                temp = i
                small = boxes[i]
        tokens += N*(small - fill)
        N = temp
        fill = small
        if N == 0:
            break
    print(tokens)
