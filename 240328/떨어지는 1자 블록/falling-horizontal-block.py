n, m, k = map(int, input().split())

grid = []

for _ in range(n):
    grid.append(list(map(int, input().split())))

place = 0
for row in range(n):
    if sum(grid[row][k - 1 : k + m - 1]) > 0:
        place = row - 1
        break

grid[place][k - 1 : k + m - 1] = [1] * m

for row in grid:
    print(*row)