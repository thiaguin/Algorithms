# Title -> Balanced Team
# Description -> codeforces.com/problemset/problem/1133/C

n = input()
skills = map(int, raw_input().split())

skills.sort()
maximum = 0
aux = {}

for i in range(n):
    if (aux.has_key(skills[i])):
        aux[skills[i]] += 1
    else:
        aux[skills[i]] = 1

for i in aux:
    total = aux[i]

    for j in range(5):
        key = i + j + 1
        total += aux[key] if aux.has_key(key) else 0

    maximum = max(maximum, total)

print(maximum)
