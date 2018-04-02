#!/bin/python3

import sys

def sockMerchant(n, ar):
    pairs = 0
    freq = Counter(ar)
    for sock in freq:
        pairs += freq[sock] // 2
    return pairs


n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = sockMerchant(n, ar)
print(result)


