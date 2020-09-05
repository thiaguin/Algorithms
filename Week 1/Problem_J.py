# Title -> Game of Robots
# Description -> codeforces.com/problemset/problem/670/B

n, k = map(int, raw_input().split())
identifiers = map(int, raw_input().split())


def getSum(n, k):
    aux = 0

    for i in range(1, n + 1):
        if (aux > 0):
            aux += i
        else:
            aux = i
        if (aux + i + 1 > k):
            return aux, i


result, index = getSum(n, k)

if (result == k):
    print(identifiers[index - 1])
else:
    print(identifiers[k - result - 1])
