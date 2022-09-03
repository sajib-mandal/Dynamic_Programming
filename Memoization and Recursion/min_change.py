# recursion without memoization

def min_change(amount, coins):
    if amount < 0:
        return float("inf")
    if amount == 0:
        return 0

    min_coins = float("inf")    # positive infinity    # negative infinity "float("-inf")
    for coin in coins:
        num_coins = 1 + min_change(amount - coin, coins)
        if num_coins < min_coins:
            min_coins = num_coins
    return min_coins

print(min_change(8, [1, 5, 4, 12]))
print(min_change(13, [1, 9, 5, 14, 30]))
print(min_change(300, [9, 7, 3]))




# recursion with memoization

def min_change(amount, coins):
    ans = _min_change(amount, coins, {})
    if ans == float("inf"):
        return -1
    else:
        return ans


def _min_change(amount, coins, memo):
    if amount in memo:
        return memo[amount]
    if amount < 0:
        return float("inf")
    if amount == 0:
        return 0

    min_coins = float("inf")
    for coin in coins:
        num_coins = 1 + _min_change(amount - coin, coins, memo)
        if num_coins < min_coins:
            min_coins = num_coins
    memo[amount] = min_coins
    return min_coins

print(min_change(8, [1, 5, 4, 12]))
print(min_change(13, [1, 9, 5, 14, 30]))
print(min_change(300, [9, 7, 3]))
print(min_change(2017, [4, 2, 10]))
