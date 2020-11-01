# Title ->Transformation: from A to B
# Description -> codeforces.com/problemset/problem/727/A

a, b = map(int, raw_input().split())
aux = [a, b]


def get_result(a, b):
    if (a > b):
        return False
    if (a == b):
        return True
    if (get_result(2 * a, b) or get_result(10 * a + 1, b)):
        aux.append(a)
        return True
    return False


result = get_result(a, b)

if (result):
    aux.sort()
    aux = map(str, list(set(aux)))
    print('YES')
    print(len(aux))
    print(' '.join(aux))
else:
    print('NO')
