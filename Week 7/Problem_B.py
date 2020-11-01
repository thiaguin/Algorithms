# Title -> New Year Transportation
# Description -> codeforces.com/problemset/problem/500/A

n, t = map(int, raw_input().split())
cells = map(int, raw_input().split())


def get_result():
    index = 1

    while (index < n):
        if (index == t):
            return 'YES'

        index += cells[index - 1]

    return 'YES' if index == t else 'NO'


print(get_result())
