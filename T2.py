#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the compareTriplets function below.
def compareTriplets(a, b):
    aPoints = 0
    bPoints = 0
    i = 0
    while i < 3:
        if (a[i] > b[i]):
            aPoints = aPoints + 1;
        if (a[i] < b[i]):
            bPoints = bPoints + 1
        i = i + 1
    return [aPoints, bPoints]

def main():
    a = list(map(int, input("Insert scores for a:").rstrip().split()))
    b = list(map(int, input("Insert scores for b:").rstrip().split()))
    result = compareTriplets(a, b)
    print("Final result:\n")
    print(' '.join(map(str, result)))

main()