def fib(n):
    table = []
    for i in range(n + 1):
        table.append(0)
    table[1] = 1
    for i in range(n):
        table[i + 1] += table[i]
        if i < len(table) - 2:
            table[i + 2] += table[i]
    return table[n]

print(fib(6))
print(fib(7))
print(fib(8))
print(fib(50))
print(fib(1000))
