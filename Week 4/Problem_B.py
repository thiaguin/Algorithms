# Title -> LCM
# Description -> codeforces.com/problemset/problem/1068/B

import math
b = input()

sqrt = int(math.ceil(math.sqrt(b)))
count = 1 if b == 1 else 2

if (sqrt > 1 and (sqrt * sqrt) == b):
    count += 1

for i in range(sqrt - 1, 1, -1):
    if (b % i == 0):
        count += 2

print(count)
