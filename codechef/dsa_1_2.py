
def rev(num):
    temp = 0
    while(num):
        temp *= 10
        temp += num % 10
        num = num // 10
    return temp


num_cases = int(input())
for case in range(1, num_cases + 1):
    print(rev(int(input())))
