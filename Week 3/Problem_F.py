# Title -> Cells Not Under Attack
# Description -> codeforces.com/problemset/problem/701/B

n, m = map(int, raw_input().split())

rows = {}
columns = {}
result = []
total = n * n

for i in range(m):
    x, y = map(int, raw_input().split())
    current = 0 if columns.has_key(y) and rows.has_key(x) else 1
    aux_rows = n - len(columns) - 1
    aux_columns = n - len((rows)) - 1

    if (not rows.has_key(x)):
        current += aux_rows
        rows[x] = True

    if (not columns.has_key(y)):
        columns[y] = True
        current += aux_columns

    total -= current
    result.append(str(total))

print(' '.join(result))
