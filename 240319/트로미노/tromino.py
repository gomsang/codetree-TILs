N, M = map(int, input().split())

grid = []
for i in range(N):
    grid.append([int(num) for num in input().split()])


def calcLshapeMax(row, col):
    return (sum([grid[row][col],
                 grid[row][col + 1],
                 grid[row + 1][col],
                 grid[row + 1][col + 1]]) -
            min(grid[row][col], grid[row][col + 1], grid[row + 1][col], grid[row + 1][col + 1]))


def calcIshapeMax(row, col):
    result = 0
    for r in range(3):
        result = max(result, grid[row + r][col] + grid[row + r][col + 1] + grid[row + r][col + 2])

    for c in range(3):
        result = max(result, grid[row][col + c] + grid[row + 1][col + c] + grid[row + 2][col + c])

    return result

# L shape calc
shapemax = 0
for row in range(N - 1):
    for col in range(M - 1):
        shapemax = max(shapemax, calcLshapeMax(row, col))
        if row < N - 2 and col < M - 2:
            shapemax = max(shapemax, calcIshapeMax(row, col))

print(shapemax)