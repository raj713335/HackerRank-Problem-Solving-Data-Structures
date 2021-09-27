#!/bin/python3

import math
import os
import random
import re
import sys
import bisect

#
# Complete the 'runningMedian' function below.
#
# The function is expected to return a DOUBLE_ARRAY.
# The function accepts INTEGER_ARRAY a as parameter.
#

def runningMedian(a):
    # Write your code here
    s = []
    t =[]
    
    for i in range(len(a)):
        bisect.insort(s,a[i])
        if (len(s))%2==0:
            t.append((s[len(s)//2]+s[(len(s)//2)-1])/2)
        else:
            t.append(s[len(s)//2])
    return t
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a_count = int(input().strip())

    a = []

    for _ in range(a_count):
        a_item = int(input().strip())
        a.append(a_item)

    result = runningMedian(a)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
