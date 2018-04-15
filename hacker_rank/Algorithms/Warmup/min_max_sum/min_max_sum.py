#!/bin/python3

import sys

def miniMaxSum(arr):
    # Complete this function
    x = sum(arr)
    print (x-(max(arr)), (x-(min(arr))))
    
if __name__ == "__main__":
    arr = list(map(int, input().strip().split(' ')))
    miniMaxSum(arr)


