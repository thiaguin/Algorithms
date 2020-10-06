# Title -> Ayoub and Lost Array
# Description -> codeforces.com/contest/1105/problem/C

size, left, right = map(int, raw_input().split())
MOD = 10 ** 9 + 7

rest = {
    0: (right / 3) - ((left - 1) / 3),
    1: ((right - 1) / 3) - ((left - 2) / 3),
    2: ((right - 2) / 3) - ((left - 3) / 3)
}

aux = [rest[0], rest[1], rest[2]]

for i in range(2, size + 1):
    aux_0 = (aux[0] * rest[0]) + (aux[1] * rest[2]) + (aux[2] * rest[1])
    aux_1 = (aux[2] * rest[2]) + (aux[0] * rest[1]) + (aux[1] * rest[0])
    aux_2 = (aux[1] * rest[1]) + (aux[0] * rest[2]) + (aux[2] * rest[0])

    aux[0] = aux_0 % MOD
    aux[1] = aux_1 % MOD
    aux[2] = aux_2 % MOD

print(aux[0])
