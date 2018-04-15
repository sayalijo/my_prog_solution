#!/bin/python3

import os
import sys

#
# Complete the breakingRecords function below.
#
def breakingRecords(score):
    high_sc = score[0]
    low_sc = score[0]
    high_cnt = 0
    low_cnt = 0
    for i in score[1:]:
        if i > high_sc:
            high_sc = i
            high_cnt += 1
        elif i < low_sc:
            low_sc = i
            low_cnt += 1
    return high_cnt, low_cnt


if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    score = list(map(int, input().rstrip().split()))

    result = breakingRecords(score)

    f.write(' '.join(map(str, result)))
    f.write('\n')

    f.close()
