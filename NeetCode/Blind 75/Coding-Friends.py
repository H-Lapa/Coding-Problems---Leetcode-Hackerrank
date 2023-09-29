#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minNum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER samDaily
#  2. INTEGER kellyDaily
#  3. INTEGER difference
#

#https://www.hackerrank.com/challenges/coding-friends/problem

def minNum(samDaily, kellyDaily, difference):
    
    #kelly cant catchup
    if kellyDaily <= samDaily:
        return -1
        
    kelly = 0
    sam = difference
    count = 0
    
    while kelly <= sam:
        
        kelly += kellyDaily
        sam += samDaily
        
        count += 1
        
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    samDaily = int(input().strip())

    kellyDaily = int(input().strip())

    difference = int(input().strip())

    result = minNum(samDaily, kellyDaily, difference)

    fptr.write(str(result) + '\n')

    fptr.close()
