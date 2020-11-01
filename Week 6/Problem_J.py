# Title -> The Fair Nut and String
# Description -> codeforces.com/contest/1084/problem/C

string = raw_input()
count = 1
MOD = 10 ** 9 + 7
aux = []
string += 'b'

for i in range(len(string)):
    if (string[i] == 'a'):
        count += 1
    if (string[i] == 'b' and count > 0):
        aux.append(count)
        count = 1

total = 1

for i in aux:
    total *= i
    total = total % MOD

print((total - 1) % MOD)
