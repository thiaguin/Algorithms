# Title -> Misha and Changing Handles
# Description -> codeforces.com/problemset/problem/501/B

n = input()

result = {}
aux = set()
count = 0

for i in range(n):
    old, new = raw_input().split()

    current_length = len(aux)
    aux.add(new)

    if (current_length != len(aux)):
        if (result.has_key(old)):
            result[new] = result[old]
            del result[old]
        else:
            result[new] = old

print(len(result))

for key in result:
    print(result[key] + ' ' + key)
