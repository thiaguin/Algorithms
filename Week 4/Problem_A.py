# Title -> Omkar and Last Class of Math
# Description -> codeforces.com/problemset/problem/1372/B

import math
t = input()


def gcd(a, b):
    if (a == 0):
        return b
    return gcd(b % a, a)


def lcm(a, b):
    return a * b / gcd(a, b)


def getResult(n):
    half = int(n / 2)
    lcms = {half: lcm(n - half, half)}

    for i in range(int(math.sqrt(n)), 0, -1):
        lcms[i] = lcm(i, n-i)

        if (i > 1 and n % i == 0):
            division = n / i
            lcms[division] = lcm(division, n - division)

    value = min(lcms, key=lcms.get)
    return (str(value) + ' ' + str(n - value))


for i in range(t):
    n = input()
    print(getResult(n))
