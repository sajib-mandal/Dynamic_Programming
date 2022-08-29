# recursion without memoization
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


print(how_sum(7, [2, 3]))
print(how_sum(7, [5, 3, 4, 7]))
print(how_sum(7, [2, 4]))
print(how_sum(8, [2, 3, 5]))
print(how_sum(300, [7, 14]))



# recursion with memoization
def how_sum(target_sum: int, numbers: list, memo={}) -> list:
    if target_sum in memo:
        return memo[target_sum]
    if target_sum == 0:
        return []
    if target_sum < 0:
        return None
    for num in numbers:
        remainder = target_sum - num
        remainder_res = how_sum(remainder, numbers, memo)
        if remainder_res is not None:
            remainder_res.append(num)
            memo[target_sum] = remainder_res
            return memo[target_sum]

    memo[target_sum] = None


print(how_sum(7, [2, 3], memo={}))
print(how_sum(7, [5, 3, 4, 7], memo={}))
print(how_sum(7, [2, 4], memo={}))
print(how_sum(8, [2, 3, 5], memo={}))
print(how_sum(300, [7, 14], memo={}))
