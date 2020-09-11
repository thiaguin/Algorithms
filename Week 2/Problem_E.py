# Title -> Remove Duplicates
# Description -> codeforces.com/problemset/problem/978/A

n = input()
sequence = raw_input().split()
aux = {}

for i in range(n-1, -1, -1):
    if (aux.has_key(sequence[i])):
        sequence.pop(i)
    else:
        aux[sequence[i]] = 1

print(len(sequence))
print(' '.join(sequence))
