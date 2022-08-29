# recursive without memoization
def best_sum(target_sum: int, numbers: list) -> list:
    if target_sum == 0:
        return []
    if target_sum < 0:
        return None
    shortest_combination = None
    for num in numbers:
        remainder = target_sum - num
        remainder_combination = best_sum(remainder, numbers)
        if remainder_combination is not None:
            remainder_combination.append(num)
            combination = remainder_combination
            if (shortest_combination is None) or (len(combination) < len(shortest_combination)):
                shortest_combination = combination
    return shortest_combination

print(best_sum(7, [5, 3, 4, 7]))
print(best_sum(8, [2, 3, 5]))
print(best_sum(8, [1, 4, 5]))
print(best_sum(100, [1, 2, 5, 25]))


# recursive with memoization

def best_sum(target_sum: int, numbers: list, memo={}) -> list:
    if target_sum in memo:
        return memo[target_sum]
    if target_sum == 0:
        return []
    if target_sum < 0:
        return None
    shortest_combination = None
    for num in numbers:
        remainder = target_sum - num
        remainder_combination = best_sum(remainder, numbers, memo)
        if remainder_combination is not None:
            remainder_combination = remainder_combination.copy()
            remainder_combination.append(num)
            combination = remainder_combination
            if (shortest_combination is None) or (len(combination) < len(shortest_combination)):
                shortest_combination = combination
    memo[target_sum] = shortest_combination
    return shortest_combination

print(best_sum(7, [5, 3, 4, 7], memo={}))
print(best_sum(8, [2, 3, 5], memo={}))
print(best_sum(8, [1, 4, 5], memo={}))
print(best_sum(100, [1, 2, 5, 25], memo={}))

