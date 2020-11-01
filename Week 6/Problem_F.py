# Title -> Guess the Array
# Description -> codeforces.com/problemset/problem/677/C

n, m, t = map(int, raw_input().split())

count = 0
tuples = []


def get_combinations(n, p):
    combinations = 1
    division = 1

    for i in range(p, n):
        combinations *= i + 1

    for i in range(1, n - p + 1):
        division *= i

    return combinations / division


for i in range(1, m + 1):
    for j in range(4, n + 1):
        if (i + j == t):
            tuples.append((j, i))


for x, y in tuples:
    boys = get_combinations(n, x)
    girls = get_combinations(m, y)
    count += boys * girls

print(count)
