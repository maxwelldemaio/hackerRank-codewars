# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 22:24:48 2020

@author: maxde
"""
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the reverseArray function below.
def reverseArray(a):
    rev = []
    for i in range(len(a)-1, -1, -1):
        rev.append(a[i])
    return rev

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = reverseArray(arr)

    fptr.write(' '.join(map(str, res)))
    fptr.write('\n')

    fptr.close()
