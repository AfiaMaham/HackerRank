#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'twoStacks' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER maxSum
#  2. INTEGER_ARRAY a
#  3. INTEGER_ARRAY b
#

def twoStacks(maxSum, a, b):
    sum_so_far = 0
    count_a = 0
    max_count = 0

    # Step 1: Take as many as possible from stack a
    while count_a < len(a) and sum_so_far + a[count_a] <= maxSum:
        sum_so_far += a[count_a]
        count_a += 1

    # Record current best count (all from A)
    max_count = count_a

    # Step 2: Now add from stack b
    count_b = 0
    # Move through stack b
    while count_b < len(b):
        sum_so_far += b[count_b]
        count_b += 1

        # If sum exceeds limit, remove from A (one by one)
        while sum_so_far > maxSum and count_a > 0:
            count_a -= 1
            sum_so_far -= a[count_a]

        # If still within maxSum, check if total picks are max
        if sum_so_far <= maxSum:
            max_count = max(max_count, count_a + count_b)

    return max_count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    g = int(input().strip())

    for g_itr in range(g):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        maxSum = int(first_multiple_input[2])

        a = list(map(int, input().rstrip().split()))

        b = list(map(int, input().rstrip().split()))

        result = twoStacks(maxSum, a, b)

        fptr.write(str(result) + '\n')

    fptr.close()
