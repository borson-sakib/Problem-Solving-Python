#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    s=len(arr)
    p=0
    n=0
    z=0
    for x in arr:
        if x>0:
            p+=1
        if x<0:
            n+=1
        if x==0:
            z+=1
    print(p/s)
    print(n/s)
    print(z/s)




if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
