

num_cases = int(input())
for case in range(1, num_cases + 1):
    cars = int(input())
    speed = list(map(int, input().split()))
    count = 1
    for i in range(1, len(speed)):
        if speed[i-1] > speed[i]:
            count += 1
        else:
            speed[i] = speed[i-1]
    print(count)
