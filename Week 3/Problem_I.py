# Title -> Beautiful Numbers
# Description -> codeforces.com/problemset/problem/1265/B

t = input()


def getResult(n, permutation):
    aux = {}
    result = ''

    for i in range(n):
        aux[permutation[i]] = i

    l = aux[1]
    r = aux[1]

    for i in range(n):
        r = max(r, aux[i + 1])
        l = min(l, aux[i + 1])

        if ((r - l) == i):
            result += '1'
        else:
            result += '0'

    return result


for i in range(t):
    n = input()
    permutation = map(int, raw_input().split())
    print(getResult(n, permutation))
