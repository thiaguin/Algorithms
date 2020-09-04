# Title -> PolandBall and Hypothesis
# Description -> codeforces.com/problemset/problem/755/A

n = input()


def getDivisor(n):
    for i in range(1, 1001):
        aux = (n * i) + 1
        for j in range(2, 1001):
            if (aux % j == 0 and aux != j):
                return i


print(getDivisor(n))
