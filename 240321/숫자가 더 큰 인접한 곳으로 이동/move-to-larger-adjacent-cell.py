n, r, c = map(int, input().split())

r -= 1
c -= 1

direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]

grid = []

for _ in range(n):
    grid.append(list(map(int, input().split())))

def find():
    global r, c
    for dir in direction:
        if 0 <= r + dir[0] <= n - 1 and 0 <= c + dir[1] <= n - 1:
            if grid[r + dir[0]][c + dir[1]] > grid[r][c]:
                r = r + dir[0]
                c = c + dir[1]
                return True
    return False


print(grid[r][c], end=' ')

while find():
    print(grid[r][c], end=' ')