#!/bin/python3

import sys

def migratoryBirds(n, ar):
    # Complete this function
    max_count = 0
    max_count_item = -1
    for i in set(ar):
        local_count = ar.count(i)
        if local_count > max_count:
            max_count = local_count
            max_count_item = i
    return max_count_item

n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = migratoryBirds(n, ar)
print(result)
