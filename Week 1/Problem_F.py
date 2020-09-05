# Title -> Broken Keyboard
# Description -> codeforces.com/problemset/problem/1251/A

t = input()


def getCharsOk(string):
    aux = 0
    ok = set()
    currentChar = string[0]

    while (aux < len(string)):
        if (aux + 1 == len(string)):
            ok.add(string[aux])
            aux += 1
        elif (string[aux] == string[aux + 1]):
            aux += 2
        else:
            ok.add(string[aux])
            aux += 1

    return ''.join(sorted(ok))


for i in range(t):
    string = raw_input()
    print(getCharsOk(string))
