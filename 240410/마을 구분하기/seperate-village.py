n = int(input())

grid = []
visited = [[False for _ in range(n)] for _ in range(n)]
directions = [(1,0), (-1,0), (0, -1), (0, 1)]

for _ in range(n):
    grid.append(list(map(int, input().split())))


def in_range(row, col):
    return 0 <= row < n and 0 <= col < n

populate = {}
def dfs(vill, row, col):
    for direction in directions:
        r, c = row + direction[0], col + direction[1]
        if not in_range(r, c):
            continue
        if grid[r][c] == 0 or visited[r][c]:
            continue
        visited[r][c] = True
        populate[vill] += 1
        dfs(vill, r, c)

vill = 0
for i in range(n):
    for j in range(n):
        if grid[i][j] == 1 and not visited[i][j]:
            populate[vill] = 1
            visited[i][j] = True
            dfs(vill, i, j)
            vill += 1

print(vill)

for p in sorted( list(populate.values())):
    print(p)