import bisect
N, X, Y = list(map(int, input().split()))
duration_list = []
for i in range(N):
    duration_list.append(list(map(int, input().split())))

incoming = list(map(int, input().split()))
outgoing = list(map(int, input().split()))
incoming.sort()
outgoing.sort()
min = outgoing[-1] - incoming[0] + 2
for dur in duration_list:
    start, end = dur[0], dur[1]
    i, j = 0, 0
    i1 = bisect.bisect_right(incoming, start)
    i2 = bisect.bisect_left(outgoing, end)
    if i1 > 0 and i2 < Y:
        time = outgoing[i2] - incoming[i1-1] + 1
        if time <= min:
            min = time

print(min)
