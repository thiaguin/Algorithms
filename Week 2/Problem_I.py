# Title -> Lecture Sleep
# Description -> codeforces.com/problemset/problem/961/B

n, k = map(int, raw_input().split())
theorems = map(int, raw_input().split())
behavior = map(int, raw_input().split())
acc = [theorems[0]]
aux = [theorems[0] * behavior[0]]
maximum = 0
index = -1
result = 0
count = 0

for i in range(1, n):
    acc.append(theorems[i] + acc[i - 1])
    aux.append((theorems[i] * behavior[i]) + aux[i - 1])

for i in range(n):
    if (behavior[i] == 0):
        max_index = min((i + k - 1), (n - 1))
        acc_current = acc[i - 1] if i > 0 else 0
        aux_current = aux[i - 1] if i > 0 else 0
        value = (acc[max_index] - acc_current) - (aux[max_index] - aux_current)
        index = i if value > maximum else index
        maximum = max(maximum, value)

result = aux[n - 1] + maximum
print(result)
