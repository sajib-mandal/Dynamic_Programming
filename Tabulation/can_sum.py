def can_sum(target_sum: int, numbers: list) -> bool:
    table = []
    for i in range(target_sum + 1):
        table.append(False)

    table[0] = True
    for i in range(len(table)):
        if table[i] == True:
            for num in numbers:
                if i + num <= target_sum:
                    table[i + num] = True
    return table[target_sum]


print(can_sum(7, [2, 3]))
print(can_sum(7, [5, 3, 4, 7]))
print(can_sum(7, [2, 4]))
print(can_sum(8, [2, 3, 5]))
print(can_sum(300, [7, 14]))
