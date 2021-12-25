for case in range(1, int(input()) + 1):
    braces = input()
    stack = []
    count = 0
    for i, brac in enumerate(braces):
        if brac == "<":
            stack.append(brac)
        else:
            if len(stack) == 0:
                break
            else:
                stack.pop()
                count = i + 1
    print(count)
