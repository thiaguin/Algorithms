# Title -> 	Levko and Permutation
# Description -> codeforces.com/problemset/problem/361/B

n, k = map(int, raw_input().split())
last = []
first = []

for i in range(1, k + 1):
    last.append(str(n - k + i))

for i in range(k + 1, n):
    first.append(str(i - k))

value = [str(n - k)] + first + last
result = '-1' if n == k else ' '.join(value)

print(result)
