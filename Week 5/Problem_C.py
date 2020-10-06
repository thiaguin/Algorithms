# Title ->  Minimum number of steps
# Description -> codeforces.com/contest/804/problem/B

string = raw_input()
index = 1
count = 0
aux = 0
flag = False
length = len(string)

for index in range(1, length):
    if (string[index - 1] == 'a'):
        aux = (((aux) + 1) * 2 - 1) % 1000000007

    if (string[index - 1] == 'a' and string[index] == 'b'):
        count += aux
        has_next = index + 1 < length
        flag = True if (has_next and string[index] == 'b') else False
    elif (flag and string[index] == 'b'):
        count += aux

print(count % 1000000007)
