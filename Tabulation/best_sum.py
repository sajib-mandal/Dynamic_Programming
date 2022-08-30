# https://www.purfe.com/dynamic-programming-learn-to-solve-algorithmic-problems-coding-challenges-python-code/#grid-tab

def best_sum(target_sum: int, numbers: list) -> list:
    table = [None for i in range(target_sum + 1)]
    table[0] = []
    for i in range(target_sum):
        if table[i] is not None:
            for num in numbers:
                if i + num <= target_sum:
                    candidate = table[i].copy()
                    candidate.append(num)
                    if table[i + num] is None or len(table[i + num]) > len(candidate):
                        table[i + num] = candidate
    return table[target_sum]


print(best_sum(7, [5, 3, 4, 7]))
print(best_sum(8, [2, 3, 5]))
print(best_sum(8, [1, 4, 5]))
print(best_sum(100, [1, 2, 5, 25]))
print(best_sum(100, [25, 1, 5, 2]))
