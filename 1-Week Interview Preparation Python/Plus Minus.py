"""
Given an array of integers, calculate the ratios of its 
elements that are positive, negative, and zero. 
Print the decimal value of each fraction on a new line with  places after the decimal.


Sample Input

STDIN           Function
-----           --------
6               arr[] size n = 6
-4 3 -9 0 4 1   arr = [-4, 3, -9, 0, 4, 1]

Sample Output

0.500000
0.333333
0.166667

"""

def plusMinus(arr):
    pos_count = 0
    neg_count = 0
    zero_count = 0

    for num in arr:
        if num > 0:
            pos_count += 1
        elif num < 0:
            neg_count += 1
        else:
            zero_count += 1

    total = len(arr)
    print(f"{pos_count / total:.6f}")
    print(f"{neg_count / total:.6f}")
    print(f"{zero_count / total:.6f}")

if __name__ == '__main__':
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    plusMinus(arr)
