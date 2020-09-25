# Title -> Divisor Subtraction
# Description -> codeforces.com/problemset/problem/1076/B

n = input()

primes = {}
aux = [True] * 1000001
start = 2

while (start <= 1000000):
    if (aux[start]):
        primes[start] = True
        for i in range(start * start, 1000001, start):
            aux[i] = False
    start += 1


def getMinimumPrimeDivisor(number):
    for prime in primes:
        if (number % prime == 0):
            return prime


def getResult(n):
    minimumDivisor = getMinimumPrimeDivisor(n)

    if (n in primes or not minimumDivisor):
        return 1
    else:
        return n / 2 if minimumDivisor == 2 else (n - minimumDivisor) / 2 + 1


print(getResult(n))
