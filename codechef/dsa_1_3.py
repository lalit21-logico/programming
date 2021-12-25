def lapindrome(string):
    f_half = sorted(string[:len(string) // 2])
    if len(string) % 2 == 0:
        s_half = sorted(string[len(string) // 2:])
    else:
        s_half = sorted(string[(len(string) // 2)+1:])
    if f_half == s_half:
        print("YES")
    else:
        print("NO")
    return


num_cases = int(input())
for case in range(1, num_cases + 1):
    lapindrome(input())
