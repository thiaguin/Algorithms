# Title -> Balanced Tunnel
# Description -> codeforces.com/problemset/problem/1237/B

n = input()
entering = map(int, raw_input().split())
exiting = map(int, raw_input().split())

enter_pointer = 0
exit_pointer = 0
count = 0
fineds = {}

while (enter_pointer < n and exit_pointer < n):
    if (fineds.has_key(entering[enter_pointer])):
        enter_pointer += 1
    elif (entering[enter_pointer] != exiting[exit_pointer]):
        fineds[exiting[exit_pointer]] = True
        exit_pointer += 1
        count += 1
    else:
        enter_pointer += 1
        exit_pointer += 1

print(count)
