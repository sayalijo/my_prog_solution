#!/bin/python3

import sys

def extraLongFactorials(n):
    fact = 1
    for i in range(2,n+1):
        fact = fact * i
    print(fact)

if __name__ == "__main__":
    n = int(input().strip())
    extraLongFactorials(n)


