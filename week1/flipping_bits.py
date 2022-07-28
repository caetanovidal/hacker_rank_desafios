#!/bin/python3

import math
import os
import random
import re
import sys

def flippingBits(n):
    bits = num_to_bits(n)
    reversed_bits = ''
    for b in bits:
        if b == '0':
            reversed_bits += '1'
        else:
            reversed_bits += '0'
    reversed_num = bits_to_num(reversed_bits)
    return reversed_num
        

def bits_to_num(bits):
    return int(bits, 2)

def num_to_bits(num):
    s = ''
    for i in range(31, -1, -1):
        cur = (num>>i) & 1
        s+= str(cur)
    return(s)

if __name__ == '__main__':
    output = flippingBits()
    print(output)
