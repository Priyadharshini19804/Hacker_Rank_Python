"""
Link: https://www.hackerrank.com/challenges/one-week-preparation-kit-jesse-and-cookies

Sample Input

STDIN               Function
-----               --------
6 7                 A[] size n = 6, k = 7
1 2 3 9 10 12       A = [1, 2, 3, 9, 10, 12]  
Sample Output

2

"""

import heapq

def cookies(k, A):
    heapq.heapify(A)
    operations = 0

    while len(A) >= 2 and A[0] < k:
        least = heapq.heappop(A)
        second_least = heapq.heappop(A)
        new_cookie = least + 2 * second_least
        heapq.heappush(A, new_cookie)
        operations += 1

    if A and A[0] >= k:
        return operations
    else:
        return -1


if __name__ == '__main__':
    n, k = map(int, input().split())  
    A = list(map(int, input().split()))   
    result = cookies(k, A)
    print(result)
