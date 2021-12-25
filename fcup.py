
no_players = int(input())
players = list(map(int, input().split()))
pillars = list(map(int, input().split()))
winner = 0
for player in players:
    if pillars[0] % player == 0 and pillars[1] % player == 0:
        winner += 1

print(winner)
