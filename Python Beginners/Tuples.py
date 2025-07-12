"""
Given an integer, , and  space-separated integers as input, create a tuple, , of those  integers. Then compute and print the result of hash(t). 

Note: hash() is one of the functions in the __builtins__ module, so it need not be imported.

Sample Input 0

2
1 2
Sample Output 0

3713081631934410656

"""

n = int(raw_input())
t = tuple(map(int, raw_input().split()))
print hash(t)
