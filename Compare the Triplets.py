#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the compareTriplets function below.
def compareTriplets(a, b):
    arr=[0,0]
    for x in range(len(a)):
        if a[x]>b[x]:
            arr[0]+=1
        elif a[x]==b[x]:
            arr[0]+=0
        else:
            arr[1]+=1
    return arr

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

