#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'birthday' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY s
#  2. INTEGER d
#  3. INTEGER m
#

def birthday(s, d, m):
    count_control = m
    lenght = len(s)
    number_of_arrays = []
    
    for i in range(0, lenght, 1):
        if i == lenght:
            break
        match_array = s[i:count_control]
        count_control += 1
        if sum(match_array) == d:
            number_of_arrays.append(match_array)
            
    return len(number_of_arrays)

if __name__ == '__main__':
    s = [4]
    d=4
    m=1
    print(birthday(s,d,m))
