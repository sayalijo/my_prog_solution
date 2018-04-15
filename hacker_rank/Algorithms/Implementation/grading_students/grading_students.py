#!/bin/python3

import sys

def solve(grades):
    # Complete this function
    base = 5
    i = 0
    for i in range(len(grades)):
        if grades[i] >= 38:
            diff = grades[i] % 5
            if diff > 2:
                grades[i] = (int(grades[i]/base) + 1) * base
    return grades

n = int(input().strip())
grades = []
grades_i = 0
for grades_i in range(n):
   grades_t = int(input().strip())
   grades.append(grades_t)
result = solve(grades)
print ("\n".join(map(str, result)))


