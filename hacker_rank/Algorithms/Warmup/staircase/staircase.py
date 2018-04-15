#!/bin/python3

import sys

def staircase(n):
    # Complete this function
    for rownum in range(n):
        print('{:>{len}}'.format('#'*(rownum+1), len = n))
        
        
if __name__ == "__main__":
    n = int(input().strip())
    staircase(n)


