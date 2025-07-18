"""

Given a square matrix, calculate the absolute difference between the sums of its diagonals.

Sample Input

3

11 2  4
4  5  6
10 8 -12

Sample Output

15
"""

n = int(input())
matrix = []

for _ in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

primary_diagonal = 0
secondary_diagonal = 0

for i in range(n):
    primary_diagonal += matrix[i][i]
    secondary_diagonal += matrix[i][n - 1 - i]

result = abs(primary_diagonal - secondary_diagonal)
print(result)
