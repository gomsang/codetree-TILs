n, m = map(int, input().split())

grid = []

visited = [[False for _ in range(n)] for _ in range(m)]

directions = [(1, 0), (0, 2)]


def in_range(row, col):
    return 0 <= row < m and 0 <= col < n


for _ in range(n):
    grid.append(list(map(int, input().split())))

escape = False


def dfs(row, col):
    global escape
    if (row, col) == (m - 1, n - 1):
        escape = True
        return

    for direction in directions:
        r, c = row + direction[0], col + direction[1]
        if not in_range(r, c):
            continue
        if not visited[r][c] and grid[r][c] == 1:
            if direction == (0, 2) and grid[r][c - 1] == 0:
                continue
            visited[r][c] = True
            dfs(r, c)


visited[0][0] = True
dfs(0, 0)

print(int(escape))