#!/bin/python3

import sys

def plusMinus(arr):
    # Complete this function
    minus_occ = 0
    plus_occ = 0
    zero_occ = 0
    for i in arr:
        if int(i) == 0:
            zero_occ += 1
        elif int(i) < 0:
            minus_occ += 1
        elif int(i) > 0:
            plus_occ += 1
    return plus_occ/len(arr), minus_occ/len(arr), zero_occ/len(arr) 
        

if __name__ == "__main__":
    n = int(input().strip())
    arr = list(map(int, input().strip().split(' ')))
    
    for i in plusMinus(arr):
        print(i)


