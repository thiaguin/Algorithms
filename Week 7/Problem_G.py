# Title -> Party
# Description -> codeforces.com/problemset/problem/217/A

n = input()
relations = {}
results = []


def get_result(value):
    if (not value in relations):
        return 1
    return 1 + get_result(relations[value])


for i in range(1, n + 1):
    p = input()

    if (p > 0):
        relations[i] = p

for i in relations:
    results.append(get_result(i))

result = 1 if len(results) == 0 else max(results)
print(result)
