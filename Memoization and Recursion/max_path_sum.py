def max_path_sum(grid):
    return _max_path_sum(grid, 0, 0)

def _max_path_sum(grid, r, c):
    if r == len(grid) or c == len(grid[0]):     # c == len(grid[0]) is inner grid : its means just pust the right broder.
        return float("-inf")

    if r == len(grid) - 1 and c == len(grid[0]) - 1:
        return grid[r][c]

    down = _max_path_sum(grid, r + 1, c)
    right = _max_path_sum(grid, r, c + 1)
    maxmum = grid[r][c] + max(down, right)
    return maxmum


grid = [
  [1, 3, 12],
  [5, 1, 1],
  [3, 6, 1],
]
print(max_path_sum(grid)) # -> 18
