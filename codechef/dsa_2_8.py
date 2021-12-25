N, K = list(map(int, input().split()))
chefs = list(map(int, input().split()))
m = 1000000007
fear = 1
stack = []
for i in range(0, len(chefs)):
    while len(stack) > 0 and chefs[i] > chefs[stack[-1]]:
        fear = (fear * ((i-stack.pop()+1)))
        fear %= m
    stack.append(i)
print(fear)
