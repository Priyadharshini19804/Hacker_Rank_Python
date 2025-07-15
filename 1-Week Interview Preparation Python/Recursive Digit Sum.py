"""

Given an integer, we need to find the super digit of the integer.

If x has only 1 digit, then its super digit is x .
Otherwise, the super digit of x is equal to the super digit of the sum of the digits of x .

For example, the super digit of 9875 will be calculated as:

  super_digit(9875)  9+8+7+5 = 29 
	super_digit(29) 	 2 + 9 = 11
	super_digit(11)		 1 + 1 = 2
	super_digit(2)		 = 2  

 """

# Read input
n, k = input().split()
k = int(k)

# Step 1: sum digits of n, multiply by k
total = sum(int(d) for d in n) * k

# Step 2: keep reducing until it's one digit
while total > 9:
    s = 0
    while total:
        s += total % 10
        total //= 10
    total = s

# Output the super digit
print(total)
