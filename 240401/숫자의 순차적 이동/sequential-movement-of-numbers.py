N, M = map(int, input().split())

grid = []


def in_range(row, col):
    return 0 <= row < N and 0 <= col < N


directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

for _ in range(N):
    grid.append(list(map(int, input().split())))

coords = {}
for row in range(N):
    for col in range(N):
        coords[grid[row][col]] = (row, col)

for num in range(16):
    row = coords[num + 1][0]
    col = coords[num + 1][1]

    max_v = 0

    for direction in directions:
        if in_range(row + direction[0], col + direction[1]) and max_v < grid[row + direction[0]][col + direction[1]]:
            max_v = grid[row + direction[0]][col + direction[1]]

    grid[coords[num + 1][0]][coords[num + 1][1]] = max_v
    grid[coords[max_v][0]][coords[max_v][1]] = num + 1
    coords[max_v], coords[num + 1] = coords[num + 1], coords[max_v] 

for row in grid:
    print(*row)