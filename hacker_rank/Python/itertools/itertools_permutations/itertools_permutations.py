from itertools import permutations
S, k = input().split(" ")
k = int(k)
for each in permutations(sorted(S), k):
    print("".join(each))
