N, M = map(int, input().split())

grid = []

directions = [(1,0), (-1,0), (0, -1), (0, 1)]

for i in range(N):
    grid.append(list(map(int, input().split())))

visited = []

def in_range(row, col):
    return 0 <= row < N and 0 <= col < M

def dfs(row, col, k):
    for direction in directions:
        r, c = row + direction[0], col + direction[1]
        if not in_range(r, c):
            continue
        if visited[r][c] or grid[r][c] <= k:
            continue
        visited[r][c] = True
        dfs(r, c, k)

max_safearea = -1
max_k = 0
for k in range(1, 101):
    visited = [[False for _ in range(M)] for _ in range(N)]
    safearea = 0
    for i in range(N):
        for j in range(M):
            if grid[i][j] > k and not visited[i][j]:
                safearea += 1
                visited[i][j] = True
                dfs(i, j, k)

    if max_safearea < safearea:
        max_safearea = safearea
        max_k = k

print(max_k, max_safearea)