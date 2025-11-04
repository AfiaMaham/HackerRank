#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'largestRectangle' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts INTEGER_ARRAY h as parameter.
#

def largestRectangle(h):
    stack = []  # to store indices
    max_area = 0
    i = 0
    n = len(h)

    while i < n:
        # If stack empty or current bar is higher, push it
        if not stack or h[i] >= h[stack[-1]]:
            stack.append(i)
            i += 1
        else:
            # Pop and calculate area
            top = stack.pop()
            height = h[top]
            # Width depends on whether stack is empty
            width = i if not stack else i - stack[-1] - 1
            max_area = max(max_area, height * width)

    # Now clear remaining bars in stack
    while stack:
        top = stack.pop()
        height = h[top]
        width = i if not stack else i - stack[-1] - 1
        max_area = max(max_area, height * width)

    return max_area

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    h = list(map(int, input().rstrip().split()))

    result = largestRectangle(h)

    fptr.write(str(result) + '\n')

    fptr.close()
