from collections import deque

n = int(input())

r1, c1, r2, c2 = map(int, input().split())

directions = [(-1, -2), (-2, -1), (-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2)]

visited = [[False for _ in range(n)] for _ in range(n)]
step = [[0 for _ in range(n)] for _ in range(n)]

q = deque()

q.append((r1 - 1,c1 - 1))
visited[r1-1][c1-1]=True

def in_range(row, col):
    return 0 <= row < n and 0 <= col < n

distance = -1
while q:
    row, col = q.popleft()
    if row == r2 - 1 and col == c2 - 1:
        distance = step[row][col]

    for direction in directions:
        r, c = row + direction[0], col + direction[1]
        if not in_range(r, c):
            continue
        if visited[r][c]:
            continue
        q.append((r, c))
        visited[r][c] = True
        step[r][c] = step[row][col] + 1

print(distance)