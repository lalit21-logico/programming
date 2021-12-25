import math


for case in range(1, int(input()) + 1):
    result = []
    string = input()
    if string == string[::-1]:
        print(string[0:math.ceil(len(string)/2)])
    else:
        sub = []
        temp = -1
        for x in range(0, len(string)-1):
            for y in range(len(string), -1, -1):
                if string[x:y] == string[x:y][::-1]:
                    sub.append(string[x:y])

            result.append(sub)
            sub = []
        print(result)
