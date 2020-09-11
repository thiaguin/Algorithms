# Title -> String Similarity
# Description -> codeforces.com/problemset/problem/1400/A

t = input()


for j in range(t):
    n = input()
    string = list(raw_input())

    result = []

    for i in range(n):
        result.append(string[2 * i])

    print(''.join(result))
