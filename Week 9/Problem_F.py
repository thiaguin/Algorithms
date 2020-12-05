# Title -> Sereja and Suffixes
# Description -> codeforces.com/problemset/problem/368/B

n, m = map(int, raw_input().split())
array = map(int, raw_input().split())
results = []
aux = {}

for i in range(len(array) - 1, -1, -1):
    aux[array[i]] = True
    results.append(len(aux))

for i in range(m):
    index = input()
    print(results[n - index])
