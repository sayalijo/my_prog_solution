#!/bin/python3

import sys

def divisibleSumPairs(n, k, ar):
    # Complete this function
    return sum(1 for i in range(n-1) for j in range(i+1, n) if int(ar[i] + ar[j]) % k == 0)

n, k = input().strip().split(' ')
n, k = [int(n), int(k)]
ar = list(map(int, input().strip().split(' ')))
result = divisibleSumPairs(n, k, ar)
print(result)
