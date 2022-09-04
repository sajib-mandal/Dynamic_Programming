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
