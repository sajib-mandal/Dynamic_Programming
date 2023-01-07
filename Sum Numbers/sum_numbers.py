# DP with Bottom-Up

def sum_numbers(n):
    # Initialize an array to store the sum of the first i numbers
    dp = [0] * (n + 1)
    # Base case
    dp[0] = 0
    # Iterate through the array and fill it with the sum of the first i numbers
    for i in range(1, n + 1):
        dp[i] = dp[i - 1] + i
    # Return the sum of the first n numbers
    return dp[n]

print(sum_numbers(4))  # prints 10
print(sum_numbers(5))  # prints 15
