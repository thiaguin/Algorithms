# Title -> Ada and Subsequence
# Description -> spoj.com/problems/ADASEQEN/en/

n, m = map(int, raw_input().split())
values = map(int, raw_input().split())

letters = 'abcdefghijklmnopqrstuvwxyz'
letters_index = {letters[i]: values[i] for i in range(len(letters))}

first = raw_input()
second = raw_input()

table = [[0 for _ in range(m + 1)] for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, m + 1):
        if (first[i - 1] == second[j - 1]):
            value = letters_index[first[i - 1]]
            table[i][j] = value + table[i - 1][j - 1]
        else:
            table[i][j] = max(table[i - 1][j], table[i][j - 1])

results = [max(row) for row in table]
print(max(results))
