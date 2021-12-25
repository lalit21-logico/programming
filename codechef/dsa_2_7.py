# for case in range(1, int(input()) + 1):
#     N, K = input().split()
#     cakes = list(map(int, input().split()))
#     counter = 0
#     max = 0
#     for i in range(0, len(cakes)):
#         if int(K) - cakes[i] > 0:
#             counter += 1
#             if max < counter:
#                 max = counter
#         else:
#             counter = 0
#     print(max)
for case in range(1, int(input()) + 1):
    N, K = list(map(int, input().split()))
    cakes = list(map(int, input().split()))
    counter = 0
    a = [-1]*(K+1)
    for i in range(N):
        counter = max(counter, i-(a[cakes[i]]+1))
        a[cakes[i]] = i
    for i in range(1, len(a)):
        counter = max(counter, N-(a[i]+1))
    print(counter)
