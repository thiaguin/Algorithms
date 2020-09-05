# Title -> Vasya and Books
# Description -> codeforces.com/problemset/problem/1073/B

n = input()
a = map(int, raw_input().split())
b = map(int, raw_input().split())

aux = {}
count = 0
result = []

for i in range(len(a)):
    aux[a[i]] = i

for j in range(len(b)):
    if (aux[b[j]] + 1 >= count):
        result.append(aux[b[j]] - count + 1)
        count = aux[b[j]] + 1
    else:
        result.append(0)

print(' '.join(map(str, result)))
