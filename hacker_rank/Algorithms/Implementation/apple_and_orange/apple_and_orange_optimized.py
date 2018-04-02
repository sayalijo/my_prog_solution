#!/bin/python3

import os
import sys

def countApplesAndOranges(s, t, a, b, apples, oranges):
    apple_count = orange_count = 0
    print(sum([1 for apple in apples if s <= a + apple <= t]))
    print(sum([1 for orange in oranges if s <= b + orange <= t]))
        

if __name__ == '__main__':
    st = input().split()

    s = int(st[0])

    t = int(st[1])

    ab = input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    apple = list(map(int, input().rstrip().split()))

    orange = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apple, orange)


