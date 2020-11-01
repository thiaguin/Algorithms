# Title -> Two Buttons
# Description -> codeforces.com/problemset/problem/520/B

n, m = map(int, raw_input().split())
result = 0

while n < m:
    result += 1 + (m % 2)
    m = (m + (m % 2)) / 2

result += n-m
print(result)
