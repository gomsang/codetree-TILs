n = int(input())

grid = []

direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]

for _ in range(n):
    grid.append(list(map(int, input().split())))

row, col = map(int, input().split())

power = grid[row - 1][col - 1]
grid[row - 1][col - 1] = 0

# 가로 축
for c in range(max(0, (col - 1) - (power - 1)), min(n, (col - 1) + (power - 1) + 1)):
    grid[row - 1][c] = 0

# 세로 축
for r in range(max(0, (row - 1) - (power - 1)), min(n, (row - 1) + (power - 1) + 1)):
    grid[r][col - 1] = 0

for c in range(n):
    lst = []
    for r in range(n):
        if grid[r][c] > 0:
            lst.append(grid[r][c])

    for r in range(n - 1, -1, -1):
        if lst:
            grid[r][c] = lst.pop()
        else:
            grid[r][c] = 0


for row in grid:
    print(*row)