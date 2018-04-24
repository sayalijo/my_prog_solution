from itertools import groupby

S = input()
l = [(len(list(j)), int(i)) for i,j in groupby(S)]
print(*l)


