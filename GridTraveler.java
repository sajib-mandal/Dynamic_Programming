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
