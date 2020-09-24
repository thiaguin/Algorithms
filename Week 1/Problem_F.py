# Title -> Broken Keyboard
# Description -> codeforces.com/problemset/problem/1251/A

t = input()
 
 
def getCharsOk(string):
    aux = 0
    ok = set()
    currentChar = string[0]
 
    while (aux < len(string)):
        if (aux + 1 == len(string) or string[aux] != string[aux + 1]):
            ok.add(string[aux])
            aux += 1
        else:
            aux += 2
 
    return ''.join(sorted(ok))
 
 
for i in range(t):
    string = raw_input()
    print(getCharsOk(string))
