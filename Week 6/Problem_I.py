# Title -> Card Game
# Description -> spoj.com/problems/HC12/

t = input()

MOD = 10 ** 9 + 7
maximum = 10 ** 6
fats = [1]

for i in range(1, maximum + 1):
    fat = i * fats[i - 1] % MOD
    fats.append(fat)


def pow_mod(a, b):
    a = a % MOD
    product = 1

    if (a == 0):
        return 0

    while (b > 0):
        if (b % 2 == 1):
            product *= a
            product = product % MOD
            b -= 1

        a = (a * a) % MOD
        b = b / 2

    return product


def get_inv(fat):
    return pow_mod(fat, MOD - 2)


def get_combination(n, p):
    value = ((fats[n] * get_inv(fats[p])) % MOD) * (get_inv(fats[n - p]) % MOD)
    return value


for i in range(t):
    n, k = map(int, raw_input().split())
    strengths = map(int, raw_input().split())

    strengths.sort()
    aux = n - 1
    count = 0

    for _ in range(k, n + 1):
        value = get_combination(aux, k-1)
        count += (value * strengths[aux]) % MOD
        count = count % MOD
        aux -= 1

    print("Case #" + str(i + 1) + ": " + str(count % MOD))
