# Title -> Tetrahedron
# Description -> codeforces.com/problemset/problem/166/E

n = input()
qualification = map(int, raw_input().split())
visiteds = {}
m = input()

results = [-1] * n

for i in range(m):
    a, b, c = map(int, raw_input().split())
    visiteds[b] = True
    surbodinate = b - 1
    value = min(c, results[surbodinate]) if results[surbodinate] >= 0 else c
    results[surbodinate] = value

result = sum(results) + 1 if len(visiteds) == (n - 1) else - 1
print(result)
