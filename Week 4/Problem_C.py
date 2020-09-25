# Title ->  Co-prime Array
# Description -> codeforces.com/problemset/problem/660/A

n = input()
integers = map(int, raw_input().split())


def gcd(a, b):
    if (a == 0):
        return b
    return gcd(b % a, a)


result = []
count = 0

for i in range(n - 1):
    gcd_result = gcd(integers[i], integers[i + 1])
    result.append(str(integers[i]))
    current_sum = integers[i] + integers[i + 1]

    if (current_sum != 2 and gcd_result != 1):
        value = 1
        result.append(str(value))
        count += 1

result.append(str(integers[n-1]))

print(count)
print(' '.join(result))
