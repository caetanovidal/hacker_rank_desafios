import math
import os
import random
import re
import sys


def timeConversion(s):
    PmAm = getPmOrAm(s)
    hours = s[0:2]
    if (PmAm == "PM"):
        if (hours != "12"):
            hours = int(hours) + 12
            converted = str(hours) + s[2:-2]
            return converted
        return s[0:-2]
    if (hours != "12"):
        converted = s[0:-2]
        return converted
    hours = "00"
    return hours + s[2:-2]

def getPmOrAm(time):
    return time[-2:]

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = "07:05:45AM"

    result = timeConversion(s)

    #fptr.write(result + '\n')

    #fptr.close()