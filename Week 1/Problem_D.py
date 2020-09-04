# Title -> C+=
# Description -> codeforces.com/problemset/problem/1368/A

t = input()


def aux(a, b, n):
    count = 0

    while (a <= n and b <= n):
        count += 1
        if (a > b):
            b += a
        else:
            a += b

    print(count)


for i in range(t):
    a, b, n = map(int, raw_input().split())
    aux(a, b, n)
