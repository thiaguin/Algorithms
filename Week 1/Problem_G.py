# Title -> New Year and Counting Cards
# Description -> codeforces.com/problemset/problem/908/A

cards = raw_input()
count = 0
vowels = ['a', 'e', 'i', 'o', 'u']

for card in cards:
    if (card.isdigit() and int(card) % 2 != 0):
        count += 1
    elif (card in vowels):
        count += 1

print(count)
