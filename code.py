#!/bin/python3

import math
import os
from collections import deque

#
# Complete the 'downToZero' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

def downToZero(n):
    queue = deque([(n, 0)])
    visited = set([n])
    while queue:
        curr, moves = queue.popleft()
        if curr == 0:
            return moves
        # Operation 2
        if curr - 1 not in visited:
            queue.append((curr - 1, moves + 1))
            visited.add(curr - 1)
        # Operation 1
        for div in range(2, int(math.sqrt(curr)) + 1):
            if curr % div:
                continue
            factor = max(div, curr // div)
            if factor not in visited:
                queue.append((factor, moves + 1))
                visited.add(factor)
    return -1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    q = int(input().strip())
    for q_itr in range(q):
        n = int(input().strip())
        result = downToZero(n)
        fptr.write(str(result) + '\n')
    fptr.close()
