# Title -> Frog Jumps
# Description -> codeforces.com/problemset/problem/1324/C

t = input()

left = 'L'
right = 'R'


def getResult(string):
    minimum = -1
    last = -1
    count = 0

    for i in range(len(string) - 1, -1, -1):
        if (minimum < 0 and string[i] == right):
            minimum = len(string) - i
            last = i
        if (minimum > 0):
            if (string[i] == right):
                minimum = last - i if last - i > minimum else minimum
                last = i
                count = 0
            else:
                count += 1

    return max((count + 1), minimum) if minimum > 0 else len(string) + 1


for i in range(t):
    string = list(raw_input())
    print(getResult(string))
