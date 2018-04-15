#!/bin/python3

import sys

def solve(n, s, d, m):
    # Complete this function
    if(n==1 and s[0]==d):
        return 1
    elif(n==1):
        return 0
    count = 0
    for i in range(len(s)-1):
        if(sum(s[i:m+i])==d):
            count = count + 1
    return count

n = int(input().strip())
s = list(map(int, input().strip().split(' ')))
d, m = input().strip().split(' ')
d, m = [int(d), int(m)]
result = solve(n, s, d, m)
print(result)


