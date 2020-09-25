# Title -> LCM Problem
# Description -> codeforces.com/problemset/problem/1389/A

n = input()

for i in range(n):
    l, r = map(int, raw_input().split())
    double = 2 * l

    if (double <= r):
        print(str(l) + ' ' + str(double))
    else:
        print("-1 -1")
