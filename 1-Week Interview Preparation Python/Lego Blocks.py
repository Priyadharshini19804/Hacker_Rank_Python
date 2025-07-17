"""

You have an infinite number of 4 types of lego blocks of sizes given as (depth x height x width):

d	h	w
1	1	1
1	1	2
1	1	3
1	1	4
Using these blocks, you want to make a wall of height  and width . Features of the wall are:

- The wall should not have any holes in it.
- The wall you build should be one solid structure, so there should not be a straight vertical break across all rows of bricks.
- The bricks must be laid horizontally.

How many ways can the wall be built?

Sample Input

STDIN   Function
-----   --------
4       t = 4
2 2     n = 2, m = 2
3 2     n = 3, m = 2
2 3     n = 2, m = 3
4 4     n = 4, m = 4
Sample Output

3  
7  
9  
3375

"""

#!/bin/python3

import os
import sys

MOD = 10**9 + 7

def legoBlocks(n, m):
    row_ways = [0] * (m + 1)
    row_ways[0] = 1
    for width in range(1, m + 1):
        for block in [1, 2, 3, 4]:
            if width - block >= 0:
                row_ways[width] += row_ways[width - block]
        row_ways[width] %= MOD

    total_ways = [pow(r, n, MOD) for r in row_ways]

    solid_ways = [0] * (m + 1)
    solid_ways[0] = 1

    for w in range(1, m + 1):
        solid_ways[w] = total_ways[w]
        for i in range(1, w):
            solid_ways[w] -= (solid_ways[i] * total_ways[w - i]) % MOD
            solid_ways[w] %= MOD

    return solid_ways[m]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    t = int(input())
    for _ in range(t):
        n, m = map(int, input().strip().split())
        result = legoBlocks(n, m)
        fptr.write(str(result) + '\n')
    fptr.close()


