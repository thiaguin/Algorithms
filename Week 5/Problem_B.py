# Title -> Kolya and Tanya
# Description -> codeforces.com/contest/584/problem/B

n = input()

permutations = 3 * 3 * 3
six_permutations = 7

aux = permutations ** n
six_aux = six_permutations ** n

result = (aux - six_aux) % 1000000007

print(result)
