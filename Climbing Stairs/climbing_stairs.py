#  DP with Bottom-Up

def climbing_stairs(n):
    # Initialize an array to store the number of ways to climb to each step
    dp = [0] * (n + 1)
    # Base Case
    dp[0] = 1
    dp[1] = 1
    # Iterate through the array and fill it with the number of ways to climb to each step
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    # Return the number of ways to climb to the top
    return dp[n]

print(climbing_stairs(3))  # prints 3
print(climbing_stairs(4))  # prints 5




# DP with Recursive(Top-Down)

