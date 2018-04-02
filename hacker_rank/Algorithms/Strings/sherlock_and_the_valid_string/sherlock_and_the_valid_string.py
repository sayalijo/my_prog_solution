#!/bin/python3

import sys

def isValid(s):
    result = 'YES'
    for each in set(s):
        if s.count(each) == 1:
            result = 'NO'
    return result

s = input().strip()
result = isValid(s)
print(result)


