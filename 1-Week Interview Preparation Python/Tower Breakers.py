"""

Two players play a game with n towers, each of height m.

Players move in turns; Player 1 goes first.

On each turn, a player chooses one tower of height h > 1, and reduces its height to x, where 1 <= x < h and x must divide h (i.e., h % x == 0).

If no such move is possible (i.e., all towers are of height 1), the current player loses.

"""

def towerBreakers(n, m):
    if m == 1 or n % 2 == 0:
        return 2
    else:
        return 1

# Input reading
t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    print(towerBreakers(n, m))
