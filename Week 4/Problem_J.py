# Title -> Vasya and Petya's Game
# Description -> codeforces.com/problemset/problem/576/A

n = input()

primes = {}
aux = [True] * (n + 1)
start = 2
quantity = {}
result = []

while (start <= n):
    if (aux[start]):
        primes[start] = True
        for i in range(start, n + 1, start):
            aux[i] = False
            quantity[i] = quantity[i] + 1 if i in quantity else 1
    start += 1

for key in quantity:
    if (quantity[key] == 1):
        result.append(str(key))


print(len(result))
print(' '.join(result))
