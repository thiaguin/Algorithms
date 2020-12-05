# Title -> Buying Apples!
# Description -> spoj.com/problems/ABA12C/en/

import sys
sys.setrecursionlimit(15000)
n, a, b, c = map(int, raw_input().split())

values = list(set([a, b, c]))
table = [[-1 for x in range(len(values))] for x in range(n+1)]
infinity = 9999999999


def dp(m, n):
    if n == 0:
        return 0
    if n < 0:
        return -infinity
    if m >= len(values) and n >= 1:
        return -infinity
    if table[n][m] == -1:
        table[n][m] = max(dp(m, n - values[m]) + 1, dp(m + 1, n))

    return table[n][m]


dp(0, n)
print(max(table[n]))
