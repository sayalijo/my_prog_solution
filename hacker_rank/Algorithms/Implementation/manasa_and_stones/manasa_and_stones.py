#!/bin/python3

import sys

def stones(n, a, b):
    a,b = min(a,b), max(a,b)
    diff = b - a
    stones = n - 1
    current_stone = a * stones
    max_stone = b * stones    
    #result = []
    if a == b:
        #result.append(current_stone)
        yield current_stone
        return result
    else:
        while current_stone <= max_stone:
            #result.append(current_stone)
            yield current_stone
            current_stone += diff
        #return result
        
        
if __name__ == "__main__":
    T = int(input().strip())
    for a0 in range(T):
        n = int(input().strip())
        a = int(input().strip())
        b = int(input().strip())
        result = stones(n, a, b)
        print(" ".join(map(str, result)))


