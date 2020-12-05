# Title -> Tetrahedron
# Description -> codeforces.com/problemset/problem/166/E

n = input()
memo = (0, 3)
MOD = 10 ** 9 + 7

for i in range(n - 2):
    x, y = memo
    value = ((2 * y)) + (3 * x)
    memo = (y, value % MOD)

if n > 2:
    print(memo[1])
else:
    print(0 if n == 1 else 3)
