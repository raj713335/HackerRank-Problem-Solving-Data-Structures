#!/bin/python3

import math
import os
import random
import re
import sys
import heapq

#
# Complete the 'cookies' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY A
#

def cookies(k, A):
    # Write your code here
    heapq.heapify(A)
    # a=heapq.heappop(A)
    # b=heapq.heappop(A)
    iterx=0
    while (A[0]<k):
        try:
            iterx+=1
            a=heapq.heappop(A)
            b=heapq.heappop(A)
            val=(a+(2*b))
            heapq.heappush(A,val)
            
        except:
            return -1
        
    
    return iterx

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    A = list(map(int, input().rstrip().split()))

    result = cookies(k, A)

    fptr.write(str(result) + '\n')

    fptr.close()
