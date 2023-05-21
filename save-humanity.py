#!/bin/python3

import math
import os
import random
import re
import sys

# https://www.hackerrank.com/challenges/save-humanity/problem?isFullScreen=true
# Complete the 'virusIndices' function below.
#
# The function accepts following parameters:
#  1. STRING p
#  2. STRING v
#
#
# Sample
#  3
#  cgatcg gc
#  atcgatcga cgg
#  aardvark ab
#
# Output
# 1 3
# 2 6
# 0 1 5
#
# 

def virusIndices(p, v):
    # Print the answer for this test case in a single line

    vLen = len(v)
    pLen = len(p)

    output = []

    for i in range(pLen - vLen + 1):
        if p[i:i+vLen] == v:
            output.append(i)
        else:
            mismatchCount = 0
            for j in range(vLen):
                if p[i+j] != v[j]:
                    mismatchCount += 1

                if mismatchCount >= 2:
                    i = i+j
                    break

            if mismatchCount < 2:
                output.append(i)

    if len(output) == 0:
        print("No Match!")
    else:
        print(*output)


if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        p = first_multiple_input[0]

        v = first_multiple_input[1]

        virusIndices(p, v)