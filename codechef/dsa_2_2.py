num_cases = int(input())
for case in range(1, num_cases + 1):
    N = int(input())
    shotlist = input()
    team_a = 0
    team_b = 0
    count = 1
    for shot in shotlist:
        if shot == "1":
            if count % 2 == 0:
                team_b += 1
            else:
                team_a += 1
        if team_b > (team_a + (N - (count//2))):
            count += 1
            break
        if team_a > (team_b + (N - (count//2))):
            count += 1
            break
        count += 1

    print(count-1)
