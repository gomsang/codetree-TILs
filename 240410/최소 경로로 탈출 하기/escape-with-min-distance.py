from collections import deque

n, m = map(int, input().split())

directions = [(-1,0), (1,0), (0,-1), (0,1)]
grid = []
visited = [[False for _ in range(m)] for _ in range(n)]
step = [[0 for _ in range(m)] for _ in range(n)]

for _ in range(n):
    grid.append(list(map(int, input().split())))

def in_range(row, col):
    return 0 <= row < n and 0 <= col < m

q = deque()
q.append((0,0))
visited[0][0] = True

distance = -1

while q:
    row, col = q.popleft()
    if row == n - 1 and col == m - 1:
        distance = step[n-1][m-1]
        break
    for direction in directions:
        r, c = row + direction[0], col + direction[1]
        if not in_range(r, c):
            continue
        if grid[r][c] == 0 or visited[r][c]:
            continue
        q.append((r, c))
        visited[r][c] = True
        step[r][c] = step[row][col] + 1

print(distance)