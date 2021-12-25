num_cases = int(input())
for case in range(1, num_cases + 1):
    activity, is_indian = input().split()
    activity = int(activity)
    laddu = 0
    for act in range(1, activity + 1):
        lst = []
        lst = input().split()
        if lst[0] == "TOP_CONTRIBUTOR":
            laddu += 300
        elif lst[0] == "CONTEST_HOSTED":
            laddu += 50
        elif lst[0] == "CONTEST_WON":
            laddu += 300
            if int(lst[1]) <= 20:
                laddu += 20 - int(lst[1])
        elif lst[0] == "BUG_FOUND":
            laddu += int(lst[1])

    if is_indian == "INDIAN":
        print(laddu // 200)
    else:
        print(laddu // 400)
