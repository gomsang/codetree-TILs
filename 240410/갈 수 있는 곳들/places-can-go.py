from collections import deque

n, k = map(int, input().split())

grid = []

directions = [(1,0), (-1,0), (0,-1), (0, 1)]

for _ in range(n):
    grid.append(list(map(int, input().split())))

visited = [[False for _ in range(n)] for _ in range(n)]

q = deque()

def in_range(row, col):
    return 0 <= row < n and 0 <= col < n

for _ in range(k):
    r, c = map(int, input().split())
    r, c = r-1,c-1
    q.append((r, c))
    visited[r][c] = True

while q:
    row, col = q.popleft()
    for direction in directions:
        r, c = row + direction[0], col + direction[1]
        if not in_range(r,c):
            continue
        if grid[r][c] == 1 or visited[r][c]:
            continue
        visited[r][c] = True
        q.append((r,c))

visitedSpace = 0
for row in visited:
    visitedSpace += sum(row)

print(visitedSpace)