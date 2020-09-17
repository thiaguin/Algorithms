# Title -> Game with string
# Description -> codeforces.com/problemset/problem/1104/B

string = list(raw_input())
stack = []
count = 0

for i in range(len(string)):
    if (len(stack) == 0):
        stack.append(string[i])
    else:
        aux = len(stack) - 1
        if (string[i] == stack[aux]):
            stack.pop(aux)
            count += 1
        else:
            stack.append(string[i])

result = 'Yes' if count % 2 == 1 else 'No'
print(result)
