#!/bin/python3

# https://www.hackerrank.com/challenges/larrys-array/problem?isFullScreen=true

import math
import os
import random
import re
import sys

'''
A		rotate 
[1,6,5,2,4,3]	[6,5,2] abc-bca 
[1,5,2,6,4,3]	[5,2,6] bca-cab
[1,2,6,5,4,3]	[5,4,3] cab-abc
[1,2,6,3,5,4]	[6,3,5]
[1,2,3,5,6,4]	[5,6,4]
[1,2,3,4,5,6]

YES
'''

#
# Complete the 'larrysArray' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER_ARRAY A as parameter.


def larrysArray(A):
    # print("A:",*A)

    try:
        for i in range(len(A)-1):
            if A[i] != i + 1:
                #print("i:", i, "Element on i:", A[i])
                target = i + 1
                targetCurIndex = A.index(target)

                #print("target: ", target)
                #print("targetCurIndex: ", targetCurIndex)
                
                swipeSingleAmount = 0
                swipeMultipleAmount = 0
                while targetCurIndex - i > 0:
                    # print("temp A:", *A)
                    if targetCurIndex - i == 1:
                        A = swipe(A, max(0,targetCurIndex-1))
                        targetCurIndex -= 1
                        swipeSingleAmount += 1
                    else:
                        A = swipe(A, max(0,targetCurIndex-2))
                        A = swipe(A, max(0,targetCurIndex-2))
                        targetCurIndex -= 2
                        swipeMultipleAmount += 2
    except:
        return "NO"

        # print("swipeSingleAmount: ", swipeSingleAmount)
        # print("swipeMultipleAmount: ", swipeMultipleAmount)
        # print("current A:", *A, "/n")
        # input()

    if checkArray(A):
        return "YES"
    else:
        return "NO"


def swipe(A, index):
    if index > len(A) - 3:
        raise Exception("Index is not valid for swiping")
    else:
        temp = A[index]
        A[index] = A[index+1]
        A[index+1] = A[index+2]
        A[index+2] = temp

    return A

def checkArray(A):

    print("check A:", *A)
    lenA = len(A)
    return A[-1] == lenA and A[-2] == (lenA - 1) and A[-3] == (lenA - 2)

# 146
# 107 47 56 66 143 118 28 113 136 119 5 87 59 18 43 67 72 6 40 34 55 122 102 103 93 86 98 79 22 141 96 123 26 132 128 24 25 125 52 112 104 94 35 15 73 44 77 46 41 1 146 4 70 91 27 32 116 23 83 58 42 127 29 16 3 63 64 60 108 69 30 82 71 57 140 131 68 8 100 45 89 7 117 49 138 120 124 37 65 126 13 48 142 144 62 61 137 88 129 33 111 81 110 145 21 92 101 105 74 106 54 36 11 31 53 17 90 78 19 135 134 95 39 51 20 121 38 85 115 133 99 97 12 75 50 80 139 2 10 84 76 114 9 14 109 130

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # t = int(input().strip())

    # for t_itr in range(t):
    #     n = int(input().strip())

    #     A = list(map(int, input().rstrip().split()))

    #     result = larrysArray(A)

    #     fptr.write(result + '\n')

    # fptr.close()

    s = "47 107 56 66 143 118 28 113 136 119 5 87 59 18 43 67 72 6 40 34 55 122 102 103 93 86 98 79 22 141 96 123 26 132 128 24 25 125 52 112 104 94 35 15 73 44 77 46 41 1 146 4 70 91 27 32 116 23 83 58 42 127 29 16 3 63 64 60 108 69 30 82 71 57 140 131 68 8 100 45 89 7 117 49 138 120 124 37 65 126 13 48 142 144 62 61 137 88 129 33 111 81 110 145 21 92 101 105 74 106 54 36 11 31 53 17 90 78 19 135 134 95 39 51 20 121 38 85 115 133 99 97 12 75 50 80 139 2 10 84 76 114 9 14 109 130"
    #s = "2 1 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25"
    A = list(map(int, s.rstrip().split(" ")))
    print("A:", *A)
    print(larrysArray(A))