#!/bin/python3

import sys

def findDigits(n):
    return sum(d != 0 and n%d == 0 for d in map(int, str(n)))

if __name__ == "__main__":
    t = int(input().strip())
    for a0 in range(t):
        n = int(input().strip())
        result = findDigits(n)
        print(result)


