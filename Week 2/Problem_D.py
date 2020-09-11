# Title -> Substring Removal Game
# Description -> codeforces.com/problemset/problem/1398/B

t = input()


def getResult(string):
    count = 0
    result = 0
    aux = []

    for i in range(len(string)):
        if (string[i] == '0' and count > 0):
            aux.append(count)
            count = 0
        if (string[i] == '1'):
            count += 1

    if (count > 0):
        aux.append(count)

    aux.sort(reverse=True)

    for i in range(0, len(aux), 2):
        result += aux[i]

    return result


for i in range(t):
    string = list(raw_input())
    print(getResult(string))
