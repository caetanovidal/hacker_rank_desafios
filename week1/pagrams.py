#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pangrams' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def pangrams(s):
    if is_pangrams(s):
        return "pangram"
    else:
        return "not pangram"

def is_pangrams(phrase):
    phrase = phrase.replace(" ", "").lower()
    dict_alphabet = make_dict_alphabet()
    for letter in phrase:
        dict_alphabet[letter] += 1
    
    for key in dict_alphabet:
        if dict_alphabet[key] >= 1:
            pangrams = True
        else:
            return False
    return pangrams
        

def make_dict_alphabet():
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    alphabet_dict_count = {}
    for letter in alphabet:
        alphabet_dict_count[letter] = 0
    return alphabet_dict_count
    

if __name__ == '__main__':
    input = "We promptly judged antique ivory buckles for the next prize"
    input2 = "We promptly judged antique ivory buckles for the prize"
    print(pangrams(input2))
