num_cases = int(input())
num_list = []
for case in range(1, num_cases + 1):
    num_list.append(int(input()))
num_list.sort()
high = 0
for i in range(0, len(num_list)):
    if high < (len(num_list)-i)*num_list[i]:
        high = (len(num_list)-i)*num_list[i]
print(high)
