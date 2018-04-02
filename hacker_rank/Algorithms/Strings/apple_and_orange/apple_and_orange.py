#!/bin/python3

import os
import sys

def countApplesAndOranges(s, t, a, b, apples, oranges):
    apple_count = 0
    orange_count = 0
    for apple in apples:
        apl_pos = a + apple
        if s <= apl_pos <= t:
            apple_count += 1
    for orange in oranges:
        org_pos = b + orange
        if s <= org_pos <= t:
            orange_count += 1
    print("{}\n{}".format(apple_count, orange_count))
            

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


