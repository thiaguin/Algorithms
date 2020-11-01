# Title -> 	Ada and Teams
# Description -> spoj.com/problems/ADATEAMS/

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


def get_result(n, a, b, d):
    schools = get_combination(n, a)
    students = get_combination(b, d)

    result = (schools * pow_mod(students, a)) % MOD

    print(result)


while True:
    try:
        n, a, b, d = map(int, raw_input().split())
        get_result(n, a, b, d)
    except EOFError:
        break
