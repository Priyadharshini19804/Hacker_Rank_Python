"""

Link: https://www.hackerrank.com/challenges/one-week-preparation-kit-simple-text-editor/

Sample Input

STDIN   Function
-----   --------
8       Q = 8
1 abc   ops[0] = '1 abc'
3 3     ops[1] = '3 3'
2 3     ...
1 xy
3 2
4 
4 
3 1
Sample Output

c
y
a

"""


text = ""
history = []
q = int(input())

for _ in range(q):
    command = input().split()

    if command[0] == "1":  # append
        history.append(text)  # save current state
        text += command[1]

    elif command[0] == "2":  # delete
        history.append(text)  # save current state
        k = int(command[1])
        text = text[:-k]

    elif command[0] == "3":  # print
        k = int(command[1])
        print(text[k - 1])  # 1-based indexing

    elif command[0] == "4":  # undo
        if history:
            text = history.pop()
