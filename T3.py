#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the staircase function below.
def staircase(n):
    i = 1
    while i <= n:
        numOfSpaces = n - i
        j = 1
        red = ""
        while j <= numOfSpaces:
            red = red + " "
            j = j + 1
        j = 1
        while j <= i:
            red = red + "#"
            j = j + 1
        print(red)
        i = i + 1

def main():
    n = int(input("Insert n:"))
    staircase(n)

main()