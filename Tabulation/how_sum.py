def how_sum(target_sum: int, numbers: list) -> list:
    table = [None for i in range(target_sum + 1)]
    table[0] = []
    for i in range(target_sum):    #  for i in range(len(table))  ; both are same
        if table[i] is not None:
            for k in numbers:
                if i + k <= target_sum:
                    table[i + k] = table[i].copy()
                    table[i + k].append(k)
    return table[target_sum]

print(how_sum(7, [2, 3]))
print(how_sum(7, [5, 3, 4, 7]))
print(how_sum(7, [2, 4]))
print(how_sum(8, [2, 3, 5]))
print(how_sum(300, [7, 14]))
