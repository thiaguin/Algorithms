# Title -> Silent Classroom
# Description -> codeforces.com/problemset/problem/1166/A

n = input()

aux = {}
count = 0


def get_combinatorial(left, right):
    result = 1

    for i in range(left, right):
        result *= (i + 1)

    return result / 2


for i in range(n):
    student = raw_input()

    if (student[0] in aux):
        aux[student[0]] += 1
    else:
        aux[student[0]] = 1

for letter in aux:
    if (aux[letter] > 2):
        first = aux[letter] / 2
        second = aux[letter] - first
        count += get_combinatorial(first - 2, first) if first > 1 else 0
        count += get_combinatorial(second - 2, second) if second > 1 else 0

print(count)
