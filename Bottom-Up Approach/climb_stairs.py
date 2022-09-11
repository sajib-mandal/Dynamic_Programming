# Time: O(n)
# Spece: O(1)


def climb_stairs(n):
    one, two = 1, 1

    for i in range(n - 1):
        temp = one
        one = one + two
        two = temp
    return one


print(climb_stairs(5))
