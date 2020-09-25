# Title -> Ehab and a Special Coloring Problem
# Description -> codeforces.com/problemset/problem/1174/C

import math

n = input()
aux = [0] * (n + 1)

count = 1
start = 2

while (start <= n):
    if (not aux[start]):
        aux[start] = count
        for i in range(start * start, n + 1, start):
            aux[i] = count
        count += 1

    start += 1

result = map(str, aux[2:])
print(' '.join(result))
