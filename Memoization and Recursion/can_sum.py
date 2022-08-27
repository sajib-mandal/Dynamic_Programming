"""
Write a function 'canSum(targetSum, numbers)' that takes in a
targetSum and an array of numbers as arguments.

The function should return a boolean indication whether or not it
is possible to generate the targetSum using numbers from the array.

You may use an element of the array as many times as needed.

You may assume that all input numbers are non-negative.
"""

# Recursion without memoization

def cansum(targetSum, numbers):
    if targetSum == 0:
        return True
    if targetSum < 0:
        return False

    for num in numbers:
        reminder = targetSum - num
        if cansum(reminder, numbers) == True:
            return True
    return False


print(cansum(7, [2, 3]))
print(cansum(7, [5, 3, 4, 7]))
print(cansum(7, [2, 4]))
print(cansum(8, [2, 3, 5]))
#print(cansum(300, [7, 14]))  not try


# recursive with memoization

def cansum(targetsum, numbers, memo=None):
    if memo is None:
        memo = dict()
    if targetsum in memo:
        return memo[targetsum]
    if targetsum == 0:
        return True
    if targetsum < 0:
        return False
    for number in numbers:
        remainder = targetsum - number
        if cansum(remainder, numbers, memo) == True:
            memo[targetsum] = True
            return True
    memo[targetsum] = False
    return False


print(cansum(7, [2, 3]))
print(cansum(7, [5, 3, 4, 7]))
print(cansum(7, [2, 4]))
print(cansum(8, [2, 3, 5]))
print(cansum(300, [7, 14]))


# next version
def cansum(targetsum, numbers, memo=None):
    if memo is None:
        memo = dict()
    if targetsum == 0:
        return True
    if targetsum < 0:
        return False
    if targetsum not in memo:
        for number in numbers:
            remainder = targetsum - number
            if cansum(remainder, numbers, memo) == True:
                memo[targetsum] = True
                return True
        memo[targetsum] = False
        return False


print(cansum(7, [2, 3]))
print(cansum(7, [5, 3, 4, 7]))
print(cansum(7, [2, 4]))
print(cansum(8, [2, 3, 5]))
print(cansum(300, [7, 14]))
