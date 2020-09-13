# Title -> Sushi for Two
# Description -> codeforces.com/problemset/problem/1138/A

n = input()
sushis = map(int, raw_input().split())
last_type = sushis[0]
aux = []
count = 1
result = 0

for i in range(1, n):
    if (sushis[i] == last_type):
        count += 1
    else:
        aux.append(count)
        last_type = sushis[i]
        count = 1

if (sushis[i] == last_type):
    aux.append(count)

for i in range(1, len(aux)):
    current = min(aux[i - 1], aux[i]) * 2
    result = max(result, current)

print(result)
