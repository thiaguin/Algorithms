# Title -> Guess the Array
# Description -> codeforces.com/contest/727/problem/C

n = input()

print('? 1 2')
x = input()

print('? 2 3')
y = input()

print('? 1 3')
z = input()

result = [(x + z - y) / 2]
result.append(x - result[0])
result.append(z - result[0])

for i in range(4, n + 1):
    print('? 1 ' + str(i))
    aux = input()
    result.append(aux - result[0])

print('! ' + ' '.join(map(str, result)))
