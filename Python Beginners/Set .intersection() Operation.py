"""
The students of District College have subscriptions to English and French newspapers. 
Some students have subscribed only to English, some have subscribed only to French, and some have subscribed to both newspapers.
You are given two sets of student roll numbers. 
One set has subscribed to the English newspaper, one set has subscribed to the French newspaper. 
Your task is to find the total number of students who have subscribed to both newspapers.

Sample Input

9
1 2 3 4 5 6 7 8 9
9
10 1 2 3 11 21 55 6 8

Sample Output

5

"""

n = int(input())
english_subscribers = set(map(int, input().split()))
m = int(input())
french_subscribers = set(map(int, input().split()))
both = english_subscribers & french_subscribers
print(len(both))
