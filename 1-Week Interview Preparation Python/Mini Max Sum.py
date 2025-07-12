"""
Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly four of the five integers. 
Then print the respective minimum and maximum values as a single line of two space-separated long integers.

Sample Input

1 2 3 4 5

Sample Output

10 14

"""

arr = list(map(int, input().split()))

total_sum = sum(arr)
min_val = min(arr)
max_val = max(arr)

min_sum = total_sum - max_val
max_sum = total_sum - min_val

print(min_sum, max_sum)
