N = int(input())
brackets = list(map(int, input().split()))
nest_pos, nesting_d = 0, 0
loop_pos, loop_d = 0, 0
stack = []
temp = 0
for i, brac in enumerate(brackets):
    if brac == 1:
        stack.append(brac)
        if len(stack) == 1:
            temp = i
    else:
        stack.pop()
        if len(stack) == 0 and loop_d < i-temp+1:
            loop_d = i-temp+1
            loop_pos = temp+1
    if len(stack) > nesting_d:
        nest_pos = i+1
        nesting_d = len(stack)

print(nesting_d, nest_pos, loop_d, loop_pos)
