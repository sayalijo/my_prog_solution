#!/bin/python3

import sys

def twoStrings(s1, s2):
    flag = 'NO'
    for char in s1:
        if char in s2:
            flag = "YES"
            break
    return flag

q = int(input().strip())
for a0 in range(q):
    s1 = input().strip()
    s2 = input().strip()
    result = twoStrings(s1, s2)
    print(result)
