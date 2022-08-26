"""
Say that you ara a traveler on a 2D grid. You begin in the
top-left corner and your goal is to travel to the bottom-right
corner. You may only move down or right.

In how many ways can you travel to the goal on a grid with
dimension m * n.
"""

# Recursive without Memoization
def gridTraveler(m, n):
    if m == 1 and n == 1:
        return 1
    if m == 0 or n == 0:
        return 0
    return gridTraveler(m - 1, n) + gridTraveler(m, n - 1)

print(gridTraveler(1, 1))
print(gridTraveler(2, 3))
print(gridTraveler(3, 2))
print(gridTraveler(3, 3))
print(gridTraveler(18, 18)) # Don't try

# Recursive with Memoization

def gridTraveler(m, n, memo = {}):
    key = str(m) + "," + str(n)

    if m == 1 and n == 1:
        return 1
    elif m == 0 or n == 0:
        return 0
    elif key in memo.keys():
        return memo[key]

    memo[key] = gridTraveler(m - 1, n, memo) + gridTraveler(m, n - 1, memo)
    return memo[key]

print(gridTraveler(4, 3))
print(gridTraveler(2, 2))
print(gridTraveler(50, 50))
print(gridTraveler(100, 100))
