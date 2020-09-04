# Title -> Minimum Integer
# Description -> codeforces.com/problemset/problem/1101/A

import math
n = input()


def solve(l, r, d):
    if (d < l or d > r):
        return d
    return math.ceil(r / d) * d + d


for i in range(n):
    l, r, d = map(int, raw_input().split())
    result = int(solve(l, r, d))
    print(result)
