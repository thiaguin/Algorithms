# Title -> T-primes
# Description -> codeforces.com/problemset/problem/230/B

import math

n = input()
integers = map(int, raw_input().split())

maximum = int(math.sqrt(max(integers)))
aux = [True for i in range(maximum + 1)]

start = 2

while (start * start <= maximum):
    if (aux[start]):
        for i in range(start * start, maximum + 1, start):
            aux[i] = False

    start += 1

for integer in integers:
    sqrt = int(math.sqrt(integer))
    isTPrime = sqrt * sqrt == integer and aux[sqrt] and integer > 3
    result = 'YES' if isTPrime else 'NO'
    print(result)
