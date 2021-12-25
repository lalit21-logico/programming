for case in range(1, int(input()) + 1):
    N = int(input())
    infix = list(input())
    postfix = ""
    stack = []
    operator = ["(", ")", "+", "-", "*", "/", "^"]
    for s in infix:
        if s in operator:
            if len(stack) == 0:
                stack.append(s)
                continue
            if s == ")":
                while(stack[-1] != "("):
                    postfix += stack.pop()
                stack.pop()
                continue
            elif s in ["+", "-"]:
                while(stack[-1] in operator[2:]):
                    postfix += stack.pop()
            elif s in ["∗", "/"]:
                while(stack[-1] in operator[4:]):
                    postfix += stack.pop()
            stack.append(s)
        else:
            postfix += s
    while(len(stack) > 0):
        postfix += stack.pop()

    print(postfix)
