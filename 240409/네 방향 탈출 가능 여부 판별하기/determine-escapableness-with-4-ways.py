from collections import deque

n, m = map(int, input().split())

grid = []

q = deque()

directions = [(-1, 0), (1,0), (0, -1), (0, 1)]

visited = [[False for _ in range(m)] for _ in range(n)]

for _ in range(n):
    grid.append(list(map(int, input().split())))

def in_range(row, col):
    return 0 <= row < n and 0 <= col < m

visited[0][0] = True
q.append((0,0))

escape = False

while q:
    row, col = q.popleft()
    if row == (n - 1) and col == (m - 1):
        escape = True
        break
    for direction in directions:
        r, c = row + direction[0], col + direction[1]

        if not in_range(r,c):
            continue

        if visited[r][c]:
            continue

        if grid[r][c] == 1:
            q.append((r,c))
            visited[r][c] = True

print(int(escape))