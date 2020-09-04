# Title -> Boy or Girl
# Description -> codeforces.com/problemset/problem/236/A

string = raw_input()

aux = {}

for i in string:
    if (not aux.has_key(i)):
        aux[i] = True

if (len(aux) % 2 == 0):
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")