# Title -> Yet Another Broken Keyboard
# Description -> codeforces.com/problemset/problem/1272/C

n, k = map(int, raw_input().split())
string = raw_input()
availables = raw_input().split()

letters_availables = {}
result = 0
count = 0

for i in range(k):
    letters_availables[availables[i]] = True

for i in range(n + 1):
    if (i == n or not string[i] in letters_availables):
        result += (count + 1) * count / 2
        count = 0
    else:
        count += 1

print(result)
