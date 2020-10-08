# Title -> Random Teams
# Description -> codeforces.com/problemset/problem/478/B

n, m = map(int, raw_input().split())


def getResult(value):
    return value * (value + 1) / 2


rest = n % m
aux = n // m

maximum = getResult(n - m)
minimum = (getResult(aux) * rest) + (getResult(aux - 1) * (m - rest))

print(str(minimum) + ' ' + str(maximum))
