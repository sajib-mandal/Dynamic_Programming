# recursive without memoization
def sum_possible(amount, numbers):
    if amount < 0:
        return False
    if amount == 0:
        return True
    for num in numbers:
        if sum_possible(amount - num, numbers) == True:
            return True
    return False

print(sum_possible(4, [1, 2, 3, 7]))
print(sum_possible(271, [10, 8, 256, 24]))

# recursion with memoization


def sum_possible(amount, numbers):  # its helper function
    return _sum_possible(amount, numbers, {})

def _sum_possible(amount, numbers, memo):
    if amount in memo:
        return memo[amount]
    if amount < 0:
        return False
    if amount == 0:
        return True

    for num in numbers:
        if _sum_possible(amount - num, numbers, memo) == True:
            memo[amount] = True
            return True
    memo[amount] = False
    return False

print(sum_possible(4, [1, 2, 3, 7]))
print(sum_possible(271, [10, 8, 256, 24]))
print(sum_possible(2017, [4, 2, 10]))
