#!/bin/python3

import sys
import time 

def timeConversion(s):
    # Complete this function
    time_struct = time.strptime(s,"%I:%M:%S%p")
    return time.strftime("%H:%M:%S", time_struct)
        

s = input().strip()
result = timeConversion(s)
print(result)


