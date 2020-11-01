# Title -> Protect Sheep
# Description -> codeforces.com/problemset/problem/948/A

r, c = map(int, raw_input().split())

farmer = []
flag = True
wolf = 'W'
sheep = 'S'
dog = 'D'
empty = '.'

for i in range(r):
    row = list(raw_input())
    farmer.append(row)

for i in range(r):
    for j in range(c):
        if (farmer[i][j] == sheep):
            if (j - 1 >= 0 and farmer[i][j - 1] == wolf):
                flag = False
            elif (j - 1 >= 0 and farmer[i][j - 1] == empty):
                farmer[i][j - 1] = dog

            if (j + 1 < c and farmer[i][j + 1] == wolf):
                flag = False
            elif (j + 1 < c and farmer[i][j + 1] == empty):
                farmer[i][j + 1] = dog

            if (i - 1 >= 0 and farmer[i - 1][j] == wolf):
                flag = False
            elif (i - 1 >= 0 and farmer[i - 1][j] == empty):
                farmer[i - 1][j] = dog

            if (i + 1 < r and farmer[i + 1][j] == wolf):
                flag = False
            elif (i + 1 < r and farmer[i + 1][j] == empty):
                farmer[i + 1][j] = dog

if (flag):
    print('Yes')
    for row in farmer:
        print(''.join(row))
else:
    print('No')
