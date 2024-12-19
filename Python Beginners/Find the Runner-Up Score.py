Task
Given the participants’ score sheet for your University Sports Day, you must find the runner-up score. You are given n scores. Store them in a list and find the score of the runner-up.


Input Format
The first line contains n. The second line contains an array A[] of n integers are each separated by a space.

Constraints
2 ≤  n ≤  10

-100 ≤  A[i] ≤ 100

Output Format
Print the runner-up score.

Output Format

Print the runner-up score.

Sample Input 0

5
2 3 6 6 5

Sample Output 0

5

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr1 = set(arr)
    arr2 = sorted(arr1)
    print(arr2[-2])
