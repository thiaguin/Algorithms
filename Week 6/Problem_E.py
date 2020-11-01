# Title -> New Year and Ascent Sequence
# Description -> codeforces.com/contest/1284/problem/B

n = input()

maximums = []
minimums = []


def add_max_and_min(array):
    minimum = array[0]
    maximum = array[0]
    flag = False

    for i in range(1, len(array)):
        if (array[i] < minimum):
            minimum = array[i]
        if (array[i] > maximum):
            maximum = array[i]
        if (array[i] > minimum):
            flag = True

    if (not flag):
        maximums.append(maximum)
        minimums.append(minimum)


for i in range(n):
    lines = map(int, raw_input().split())
    integers = lines[1:]
    add_max_and_min(integers)

maximums.sort()
minimums.sort()
length = len(maximums)
total = ((n - length) ** 2) + ((n - length) * length * 2)
count = 0
index = 0

while (count < length and index < length):
    if (minimums[index] < maximums[count] and index < length):
        index += 1
    else:
        total += index
        count += 1

total += (length - count) * index

print(total)
