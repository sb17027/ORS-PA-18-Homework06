#!/bin/python3
import os
import sys

#
# Complete the simpleArraySum function below.
#
def simpleArraySum(ar):
    i = 0
    res = 0
    while i < len(ar):
        res = res + ar[i]
        i = i + 1
    return res


def main():
    ar_count = int(input())
    ar = list(map(int, input().rstrip().split()))
    result = simpleArraySum(ar)
    print(str(result) + '\n')

main()
