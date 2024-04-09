n = int(input())

directions = [(1,0), (-1, 0), (0,-1), (0,1)]

grid = []

visited = []

for _ in range(n):
    grid.append(list(map(int,input().split())))

def in_range(row, col):
    return 0 <= row < n and 0 <= col < n

count = 0
count_max = 0
explodes = 0

def dfs(num, row, col):
    global count
    for direction in directions:
        r, c = row + direction[0], col + direction[1]
        if not in_range(r, c):
            continue
        if not visited[r][c] and grid[r][c] == num:
            visited[r][c] = True
            count += 1
            dfs(num, r, c)

for num in range(1, 101):
    visited = [[False for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if not visited[i][j] and grid[i][j] == num:
                count = 1
                visited[i][j] = True
                dfs(num, i, j)
                count_max = max(count, count_max)
                if count >= 4:
                    explodes += 1

print(explodes, count_max)