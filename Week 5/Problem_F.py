# Title -> Guess the Array
# Description -> codeforces.com/problemset/problem/677/C

string = raw_input()
values = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz-_'
aux = {}
result = 1
MOD = 10 ** 9 + 7

for i in range(len(values)):
    aux[values[i]] = i


for char in string:
    binary = bin(aux[char]).split('b')[1]
    zeros = 6 - len(binary)

    for j in binary:
        if (j == '0'):
            zeros += 1

    result *= ((3 ** zeros) or 1)
    result = result % MOD

print(result % MOD)
