# Title -> Registration system
# Description -> codeforces.com/problemset/problem/4/C

n = input()
aux = {}


def getResponse(name):
    result = 'OK'

    if (aux.has_key(name)):
        result = name + str(aux[name])
        aux[name] += 1
    else:
        aux[name] = 1

    return result


for i in range(n):
    name = raw_input()
    print(getResponse(name)
