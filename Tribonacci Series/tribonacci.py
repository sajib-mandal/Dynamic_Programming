# recursive without memoization

def tribonacci(n):
    if n <= 1:   # if n == 0 or n == 1:
        return 0
    if n == 2:
        return 1
    return tribonacci(n - 1) + tribonacci(n - 2) + tribonacci(n - 3)

print(tribonacci(5))


# recursive with memoization


def tribonacci(n):    # its helper function
    return _tribonacci(n, {})

def _tribonacci(n, memo):
    if n in memo:
        return memo[n]
    if n <= 1:   #if n == 0 or n == 1:
        return 0
    if n == 2:
        return 1
    memo[n] = _tribonacci(n - 1, memo) + _tribonacci(n - 2, memo) + _tribonacci(n - 3, memo)
    return memo[n]


print(tribonacci(5))
print(tribonacci(100))
