# Title -> Table Tennis
# Description -> codeforces.com/problemset/problem/879/B

n, k = map(int, raw_input().split())
powers = map(int, raw_input().split())

winner = powers[0]
wins = 0
index = 1

while (wins < k and len(powers) > index):
    if (powers[index] > winner):
        winner = powers[index]
        wins = 1
    else:
        wins += 1

    index += 1

print(winner)
