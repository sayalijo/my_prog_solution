from itertools import combinations
S,k = input().split(" ")
k = int(k)
for i in range(1, k+1):
    for each in combinations(sorted(S), i):
        print("".join(each))
