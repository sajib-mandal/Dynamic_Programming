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

def climbing_stairsR(n, memo):
    # Base case
    if n <= 1:
        return 1
    # Recursive case
    if memo[n] > 0:
        return memo[n]
    
    memo[n] = climbing_stairsR(n - 1, memo) + climbing_stairsR(n - 2, memo)
    return memo[n]

def climb_stairs_wrapper(n):
    # Initialize an array to store the number of ways to climb to each step
    memo = [0] * (n + 1)
    return climbing_stairsR(n, memo)

print(climb_stairs_wrapper(4))  # prints 5
print(climb_stairs_wrapper(5))  # prints 8
