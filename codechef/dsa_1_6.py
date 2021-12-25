num_cases = int(input())
for case in range(1, num_cases + 1):
    num = int(input())
    count = 0
    while(num >= 5):
        num //= 5
        count += num

    print(count)
