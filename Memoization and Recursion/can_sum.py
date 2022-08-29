"""
Write a function 'canSum(targetSum, numbers)' that takes in a
targetSum and an array of numbers as arguments.

The function should return a boolean indication whether or not it
is possible to generate the targetSum using numbers from the array.

You may use an element of the array as many times as needed.

You may assume that all input numbers are non-negative.
"""

# Recursion without memoization
def how_sum(target_sum: int, numbers: list) -> list:
    if target_sum == 0:
        return []
    if target_sum < 0:
        return None
    for num in numbers:
        remainder = target_sum - num
        remainder_res = how_sum(remainder, numbers)
        if remainder_res is not None:
            remainder_res.append(num)
            return remainder_res
    return None


print(can_sum(7, [2, 3]))
print(can_sum(7, [5, 3, 4, 7]))
print(can_sum(7, [2, 4]))
print(can_sum(8, [2, 3, 5]))
print(can_sum(300, [7, 14]))


# recursion with memoization

def can_sum(target_sum: int, numbers: list, memo={}) -> bool:
    if target_sum in memo:
        return memo[target_sum]
    if target_sum == 0:
        return True
    if target_sum < 0:
        return False
    for num in numbers:
        remainder = target_sum - num
        if can_sum(remainder, numbers, memo):
            memo[target_sum] = True
            return memo[target_sum]

    memo[target_sum] = False
    return memo[target_sum]


print(can_sum(7, [2, 3], memo={}))
print(can_sum(7, [5, 3, 4, 7], memo={}))
print(can_sum(7, [2, 4], memo={}))
print(can_sum(8, [2, 3, 5], memo={}))
print(can_sum(300, [7, 14], memo={}))
