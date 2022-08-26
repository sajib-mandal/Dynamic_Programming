# recursive without memoization

def fibonacci(n):
    if n <= 2:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(6))
print(fibonacci(7))
print(fibonacci(8))



# recursive with memoization

def fibonacci(n, memo = {}):
    if n in memo:
        return memo[n]
    if n <= 2:
        return 1
    memo[n] = fibonacci(n - 1, memo) + fibonacci(n - 2, memo)
    return memo[n]


print(fibonacci(6))
print(fibonacci(7))
print(fibonacci(8))
print(fibonacci(50))


# 3rd version
def fib(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 2:
        return 1
    if n not in memo:
        memo[n] = fib(n - 1, memo) + fib(n - 2, memo)
    return memo[n]


print(fib(6))
print(fib(7))
print(fib(8))
print(fib(50))
