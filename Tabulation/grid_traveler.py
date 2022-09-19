def grid_traveler(m, n):
    table = []
    for i in range(m + 1):
        table.append([0 for j in range(n + 1)])
    table[1][1] = 1
    for i in range(m + 1):
        for j in range(n + 1):
            current = table[i][j]
            if j + 1 <= n:
                table[i][j + 1] += current
            if i + 1 <= m:
                table[i + 1][j] += current
    return table[m][n]

print(grid_traveler(1, 1))
print(grid_traveler(2, 3))
print(grid_traveler(3, 2))
print(grid_traveler(3, 3))
print(grid_traveler(18, 18))



def grid_traveler(m, n):
    if 1 == m or 1 == n:
        return 1

    dp = [[1 for j in range(n)] for i in range(m)]

    for y in range(1, m):
        for x in range(1, n):
            dp[y][x] = dp[y - 1][x] + dp[y][x - 1]

    return dp[-1][-1]

print(grid_traveler(1, 1))
print(grid_traveler(2, 3))
print(grid_traveler(3, 2))
print(grid_traveler(3, 3))
print(grid_traveler(18, 18))
