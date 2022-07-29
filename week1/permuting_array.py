#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'twoArrays' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY A
#  3. INTEGER_ARRAY B
#

def twoArrays(k, A, B):
    # a' b' >= k
    A = sorted(A)
    B = sorted(B, reverse=True)
    for i in range(len(B)):
        if A[i] + B[i] >= k:
            pass
        else:
            return "NO"
    return "YES"

if __name__ == '__main__':
    a = [2, 1, 3]
    b = [7, 8, 9]
    k = 10
    a2 = [1, 2, 2, 1]
    b2 = [3, 3, 3, 4]
    k2 = 5
    print(twoArrays(k2, a2, b2))
