# recursive without memoization

def max_path_sum(grid):
    return _max_path_sum(grid, 0, 0)

def _max_path_sum(grid, r, c):
    if r == len(grid) or c == len(grid[0]):     # c == len(grid[0]) is inner grid : its means just pust the right broder.
        return float("-inf")

    if r == len(grid) - 1 and c == len(grid[0]) - 1:
        return grid[r][c]

    down = _max_path_sum(grid, r + 1, c)
    right = _max_path_sum(grid, r, c + 1)
    maximum = grid[r][c] + max(down, right)
    return maximum


grid = [
  [1, 3, 12],
  [5, 1, 1],
  [3, 6, 1],
]
print(max_path_sum(grid)) # -> 18


# recursive with memoization

def max_path_sum(grid):
    return _max_path_sum(grid, 0, 0, {})

def _max_path_sum(grid, r, c, memo):
    pos = (r, c)
    if pos in memo:
        return memo[pos]
    if r == len(grid) or c == len(grid[0]):     # c == len(grid[0]) is inner grid : its means just pust the right broder.
        return float("-inf")

    if r == len(grid) - 1 and c == len(grid[0]) - 1:
        return grid[r][c]

    down = _max_path_sum(grid, r + 1, c, memo)
    right = _max_path_sum(grid, r, c + 1, memo)
    maximum = grid[r][c] + max(down, right)
    memo[pos] = maximum
    return maximum


grid = [
  [1, 3, 12],
  [5, 1, 1],
  [3, 6, 1],
]
print(max_path_sum(grid)) # -> 18

grid = [
  [1, 2, 8,  1],
  [3, 1, 12, 10],
  [4, 0, 6,  3],
]
print(max_path_sum(grid)) # -> 36

grid = [
  [1, 2, 8, 1],
  [3, 10, 12, 10],
  [4, 0, 6, 3],
]
print(max_path_sum(grid)) # -> 39

grid = [
  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]
print(max_path_sum(grid)) # -> 27


grid = [
  [1, 1, 3, 1, 1, 1, 1, 4, 1, 1, 1, 1, 1],
  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
  [1, 2, 1, 1, 6, 1, 1, 5, 1, 1, 0, 0, 1],
  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
  [1, 1, 1, 5, 1, 1, 1, 1, 0, 1, 1, 1, 1],
  [2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
  [2, 1, 1, 1, 1, 8, 1, 1, 1, 1, 1, 1, 1],
  [2, 1, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
  [1, 1, 1, 1, 1, 1, 1, 9, 1, 1, 1, 1, 1],
  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
  [1, 1, 1, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1],
  [1, 1, 1, 1, 1, 1, 1, 1, 1, 8, 1, 1, 1],
  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]
print(max_path_sum(grid)) # -> 56
