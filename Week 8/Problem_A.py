# Title -> Where do I Turn?
# Description -> codeforces.com/problemset/problem/227/A

x_a, y_a = map(int, raw_input().split())
x_b, y_b = map(int, raw_input().split())
x_c, y_c = map(int, raw_input().split())

position = ((x_b - x_a) * (y_c - y_a)) - ((y_b - y_a) * (x_c - x_a))
result = ''

if (position == 0):
    result = 'TOWARDS'
else:
    result = 'RIGHT' if position < 0 else 'LEFT'

print(result)
