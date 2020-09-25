# Title -> Heidi Learns Hashing (Easy)
# Description -> codeforces.com/problemset/problem/1184/A1

import math
n = input()


def getResult(n):
    sqrt = int(math.ceil(math.sqrt(n)))

    for i in range(1, sqrt):
        dividend = n - (i * i) - i - 1
        divider = 2 * i

        result = float(dividend) / float(divider)

        if (result.is_integer() and result > 0):
            return str(i) + ' ' + str(int(result))

    return 'NO'


print(getResult(n))
