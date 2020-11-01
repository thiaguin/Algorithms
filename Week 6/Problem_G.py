# Title -> The last digit
# Description -> https://www.spoj.com/problems/LASTDIG/

t = input()


def getFinals(number):
    aux = []

    for i in range(1, 11):
        value = (number ** i) % 10

        if (value in aux):
            return aux

        aux.append(value)

    return aux


for i in range(t):
    a, b = map(int, raw_input().split())
    finals = getFinals(a % 10)
    index = b % len(finals)
    result = finals[index - 1] if (b > 0) else 1
    print(result)
