# Title -> Shuffle Hashing
# Description -> codeforces.com/problemset/problem/1278/A

t = input()


def decrypt(password, hashed, count):
    if (len(password) == 0):
        return 'YES'
    if (len(hashed) < len(password) or len(hashed) == 0):
        return 'NO'

    first_hashed = hashed.pop(0)

    if (first_hashed in password):
        index = password.index(first_hashed)
        password.pop(index)
        count += 1
        return decrypt(password, hashed, count)
    else:
        return decrypt(list(p), hashed, 0)


def getResult(p, h):
    result = 'NO'

    while (len(h) >= len(p)):
        match = decrypt(list(p), list(h), 0)

        if (match == 'YES'):
            return match
        else:
            h.pop(0)

    return result


for i in range(t):
    p = list(raw_input())
    h = list(raw_input())
    print(getResult(p, h))
