# Title -> Secret Passwords
# Description -> codeforces.com/problemset/problem/1263/D

n = input()
visiteds = {}
aux = {}
count = 0


def dfs(value):
    if (not value in visiteds):
        visiteds[value] = True

        for key in aux:
            if (value in aux[key]):
                dfs(key)


def add_dict(array, dictionary):
    for element in array:
        dictionary[element] = True

    return dictionary


for i in range(n):
    row = list(set(list(raw_input())))
    if (row[0] in aux):
        add_dict(row, aux[row[0]])
    else:
        aux[row[0]] = add_dict(row, {})


for letter in aux:
    if (not letter in visiteds):
        count += 1
        aux_dict = []

        for char in aux:
            if letter in aux[char]:
                for element in aux[char]:
                    dfs(element)

        for key in visiteds:
            if (key in aux):
                for value in aux[key]:
                    aux_dict.append(value)

        for el in aux_dict:
            visiteds[el] = True

print(count)
