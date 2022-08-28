def fib(n):                             # F = {}
    F = {0: 0, 1: 1}                    # F[0], F[1] = 0, 1        
    for i in range(2, n + 1):
        F[i] = F[i - 1] + F[i - 2]
    return F[n]

print(fib(6))
print(fib(7))
print(fib(8))
print(fib(50))
