# Title -> The Knapsack Problem
# Description -> spoj.com/problems/KNAPSACK/en/

s, n = map(int, raw_input().split())
values = []
sizes = []

for i in range(n):
    size, value = map(int, raw_input().split())
    values.append(value)
    sizes.append(size)

memo = [[0 for x in range(s + 1)] for x in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, s + 1):
        if sizes[i - 1] <= j:
            memo[i][j] = max(values[i-1] + memo[i-1]
                             [j-sizes[i-1]], memo[i-1][j])
        else:
            memo[i][j] = memo[i - 1][j]

print(memo[n][s])
