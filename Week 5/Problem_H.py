# Title -> 	Modulo Equality
# Description -> codeforces.com/problemset/problem/1269/B

n, m = map(int, raw_input().split())
first = map(int, raw_input().split())
second = map(int, raw_input().split())

first.sort()
second.sort()

results = {}

for i in range(n):
    diff = (second[0] - first[i]) % m
    results[diff] = True

results = list(results.keys())
results.sort()


def get_result():
    for i in results:
        aux = []

        for j in range(n):
            value = (first[j] + i) % m
            aux.append(value)

        aux.sort()

        if (aux == second):
            return i


print(get_result())
