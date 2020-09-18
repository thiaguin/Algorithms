# Title -> Build a Contest
# Description -> codeforces.com/problemset/problem/1100/B

n, m = map(int, raw_input().split())
problems = map(int, raw_input().split())

aux = {}
result = []


def remove():
    removeds = []

    for i in aux:
        if (aux[i] == 1):
            removeds.append(i)
        else:
            aux[i] -= 1

    for i in removeds:
        del aux[i]


for i in range(m):
    if (aux.has_key(problems[i])):
        aux[problems[i]] += 1
    else:
        aux[problems[i]] = 1

    if (len(aux) == n):
        result.append('1')
        remove()
    else:
        result.append('0')

print(''.join(result))
