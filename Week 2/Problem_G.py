# Title -> K-th Not Divisible by n
# Description -> codeforces.com/problemset/problem/1352/C

import math
t = input()


def getResult(n, k):
    division = int(math.floor(k / n))
    result = k + division
    aux = n * (division + 1)
    extra = 0
    jumped = result - aux

    while (aux > k and aux < result):
        extra = (jumped / n) + 1
        division_aux = math.floor(result / n)
        aux = n * int(division_aux + 1)
        result += extra
        jumped = result - aux

    if (result % n == 0):
        result += 1

    return result


for i in range(t):
    n, k = map(int, raw_input().split())
    print(getResult(n, k))
