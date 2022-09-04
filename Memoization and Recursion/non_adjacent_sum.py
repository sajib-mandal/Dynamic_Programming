# recursive without memoization

"""
For example, given:
[2, 4, 5, 12, 7]
The maximum non-adjacent sum is 16, because 4 + 12.
4 and 12 are not adjacent in the list.
"""

def non_adjacent_sum(nums):
    return _non_adjacent_sum(nums, 0)

def _non_adjacent_sum(nums, i):
    if i >= len(nums):
        return 0

    include = nums[i] + _non_adjacent_sum(nums, i + 2)
    exclude = _non_adjacent_sum(nums, i + 1)
    return max(include, exclude)

nums = [2, 4, 5, 12, 7]
print(non_adjacent_sum(nums)) # -> 16

nums = [7, 5, 5, 12]
print(non_adjacent_sum(nums)) # -> 19

nums = [7, 5, 5, 12, 17, 29]
print(non_adjacent_sum(nums)) # -> 48


# recursion with memoization


def non_adjacent_sum(nums):
    return _non_adjacent_sum(nums, 0, {})

def _non_adjacent_sum(nums, i, memo):
    if i in memo:
        return memo[i]
    if i >= len(nums):
        return 0

    include = nums[i] + _non_adjacent_sum(nums, i + 2, memo)
    exclude = _non_adjacent_sum(nums, i + 1, memo)
    memo[i] = max(include, exclude)
    return memo[i]

nums = [2, 4, 5, 12, 7]
print(non_adjacent_sum(nums)) # -> 16

nums = [7, 5, 5, 12]
print(non_adjacent_sum(nums)) # -> 19

nums = [7, 5, 5, 12, 17, 29]
print(non_adjacent_sum(nums)) # -> 48

nums = [
  72, 62, 10,  6, 20, 19, 42,
  46, 24, 78, 30, 41, 75, 38,
  23, 28, 66, 55, 12, 17, 9,
  12, 3, 1, 19, 30, 50, 20
]
print(non_adjacent_sum(nums)) # -> 488

nums = [
  72, 62, 10,  6, 20, 19, 42, 46, 24, 78,
  30, 41, 75, 38, 23, 28, 66, 55, 12, 17,
  83, 80, 56, 68,  6, 22, 56, 96, 77, 98,
  61, 20,  0, 76, 53, 74,  8, 22, 92, 37,
  30, 41, 75, 38, 23, 28, 66, 55, 12, 17,
  72, 62, 10,  6, 20, 19, 42, 46, 24, 78,
  42
]
print(non_adjacent_sum(nums)) # -> 1465
