"""

Given an array of integers, where all elements but one occur twice, find the unique element.

Input 

5
0 0 1 2 1

Output

2
"""

size = int(input())                   # Read size, e.g., 3
a = list(map(int, input().split()))  # Read 3 integers in one line

result = 0
for num in a:
    result ^= num

print(result)
