from collections import deque

n, k = map(int, input().split())

grid = []

directions = [(1, 0), (-1, 0), (0, -1), (0, 1)]

for _ in range(n):
    grid.append(list(map(int, input().split())))

r, c = map(int, input().split())


def in_range(row, col):
    return 0 <= row < n and 0 <= col < n


def bfs(start_r, start_c):
    q = deque()
    visited = [[False for _ in range(n)] for _ in range(n)]
    q.append((start_r, start_c))
    visited[start_r][start_c] = True

    max_v = 0
    best_pos = (n, n)

    while q:
        row, col = q.popleft()
        # print("traverse", row, col)
        for direction in directions:
            r, c = row + direction[0], col + direction[1]
            # print("consider", r, c)
            if not in_range(r, c):
                continue
            if visited[r][c]:
                continue
            if grid[start_r][start_c] < grid[r][c]:
                continue
            q.append((r, c))
            visited[r][c] = True

            if max_v <= grid[r][c]:
                max_v = grid[r][c]
                if r < best_pos[0] or (r == best_pos[0] and c <= best_pos[1]):
                    best_pos = (r, c)
    return best_pos


r, c = r - 1, c - 1
for _ in range(k):
    b_r, b_c = bfs(r, c)
    # print((b_r, b_c))
    if (b_r, b_c) == (n, n):
        break
    r, c = b_r, b_c

print(r + 1, c + 1)