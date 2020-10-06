# Title -> Pocket Book
# Description -> codeforces.com/contest/152/problem/C

n, m = map(int, raw_input().split())

aux = 1
names = []

for i in range(n):
    name = raw_input()
    names.append(name)


for i in range(m):
    current_aux = {}

    for j in range(n):
        current_name = names[j]
        if (not current_name[i] in current_aux):
            current_aux[current_name[i]] = True

    aux = aux * len(current_aux)

    if (aux > 1000000007):
        aux = aux % 1000000007

print(aux)
