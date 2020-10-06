# Title -> Modular Equations
# Description -> codeforces.com/problemset/problem/495/B

import math
a, b = map(int, raw_input().split())


def getQuantityDivisor(number, aux):
    sqrt = math.sqrt(number)

    count = 0
    start = 2 if (aux != 0) else 1

    for i in range(start, int(sqrt) + 1):
        if (number % i == 0):
            if ((number / i) > aux):
                count += 1
            if (i > aux and i != (number / i)):
                count += 1

    return count


if (a == b):
    print('infinity')
elif (b > a):
    print(0)
elif (b < a):
    aux = a - b
    value = 1 if (b != 0 and a % aux == b) else 0
    result = value + getQuantityDivisor(aux, b)
    print(result)
