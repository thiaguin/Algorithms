# Title -> Lineland Mail
# Description -> codeforces.com/problemset/problem/567/A

n = input()
cities = map(int, raw_input().split())
aux = [0]


def getValues(index):
    if (i == 0):
        return aux[1], aux[n - 1] - aux[0]
    if (i == n - 1):
        return aux[n - 1] - aux[n - 2], aux[n - 1] - aux[0]

    previous = aux[index] - aux[index - 1]
    following = aux[index + 1] - aux[index]
    first = aux[index] - aux[0]
    last = aux[n - 1] - aux[index]

    minimun = min(previous, following)
    maximum = max(first, last)

    return minimun, maximum


for i in range(1, len(cities)):
    aux.append(abs(cities[i] - cities[i - 1]) + aux[i - 1])

for i in range(len(cities)):
    minimun, maximum = getValues(i)
    print(str(minimun) + ' ' + str(maximum))
