direction_grid = [(1, 0), (0, 1), (-1, 0), (0, -1)]

# 우 하 좌 상
direction = 0

n = int(input())
x, y = map(int, input().split())

grid = []

for row in range(n):
    grid.append(list(input()))


def avilable(x, y):
    if not (1 <= x <= n and 1 <= y <= n): return True
    if grid[y - 1][x - 1] == "#":
        return False
    return True


def rightwallchk(x, y):
    if not (1 <= x <= n and 1 <= y <= n): return True
    if grid[y - 1][x - 1] == "#":
        return True
    return False


iso_cnt = 0
t = 0
while (True):
    if iso_cnt >= 4:
        t = -1
        break
    if avilable(x + direction_grid[direction][0], y + direction_grid[direction][1]):
        iso_cnt = 0
        if not (1 <= x + direction_grid[direction][0] <= n and 1 <= y + direction_grid[direction][1] <= n):
            t += 1
            break
        if not avilable(x + direction_grid[direction][0] + direction_grid[(direction + 1) % 4][0],
                        y + direction_grid[direction][1] + direction_grid[(direction + 1) % 4][1]):
            t += 1
            x = x + direction_grid[direction][0]
            y = y + direction_grid[direction][1]
            if not rightwallchk(x + direction_grid[(direction + 1) % 4][0], y + direction_grid[(direction + 1) % 4][1]):
                t = -1
                break
        else:
            x = x + direction_grid[direction][0]
            y = y + direction_grid[direction][1]
            direction = (direction + 1) % 4
            x = x + direction_grid[direction][0]
            y = y + direction_grid[direction][1]
            t += 2
            if not rightwallchk(x + direction_grid[(direction + 1) % 4][0], y + direction_grid[(direction + 1) % 4][1]):
                t = -1
                break
    else:
        iso_cnt += 1
        direction = (direction - 1) % 4

    if t >= n * n:
        t = -1
        break

print(t)