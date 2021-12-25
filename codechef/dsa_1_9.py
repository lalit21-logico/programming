def IsMultiple(K, d_zero, d_one):
    sum = d_zero + d_one
    c = (2*sum) % 10 + (4*sum) % 10 + (6*sum) % 10 + (8*sum) % 10
    cycles = (K-3)//4
    ans = sum+(sum % 10) + (c*cycles)
    left = (K-3)-(cycles*4)
    p = 2
    for i in range(1, int(left)+1):
        ans += (p*sum) % 10
        p = (p*2) % 10
    if (ans % 3 == 0):
        print("YES")
    else:
        print("NO")


num_cases = int(input())
for case in range(1, num_cases + 1):
    K, d_zero, d_one = input().split()
    K, d_zero, d_one = int(K), int(d_zero), int(d_one)
    if (K == 2):
        if ((d_zero+d_one) % 3 == 0):
            print("YES")
        else:
            print("NO")
        continue
    IsMultiple(K, d_zero, d_one)
