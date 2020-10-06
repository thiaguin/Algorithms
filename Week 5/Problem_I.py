# Title -> Just Add It
# Description -> spoj.com/problems/ZSUM/

n, k = map(int, raw_input().split())

count = 0
aux = 0
MOD = 10000007

aux_1 = 0
aux_2 = 0


def getPow(base, exp):
    result = 1

    while (exp > 0):
        if (exp % 2 == 1):
            result = (result * base) % MOD
        base = (base * base) % MOD
        exp = exp // 2

    return result


while (n != 0 and k != 0):
    current_s = getPow(n, k) % MOD
    current_p = getPow(n, n) % MOD

    previous_s = (2 * getPow(n - 1, k)) % MOD
    previous_p = (2 * getPow(n - 1, n - 1)) % MOD

    result = (current_p + current_s + previous_p + previous_s) % MOD
    print(result)

    n, k = map(int, raw_input().split())
