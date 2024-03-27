import copy

n, m, t = map(int, input().split())

grid = []

grid_direction = [(-1,0), (1,0), (0, -1), (0,1)]

for row in range(n):
    grid.append(list(map(int, input().split())))

balls = [[0 for _ in range(n)] for _ in range(n)]

def in_range(row, col):
    return (0 <= row < n) and (0 <= col < n)

for _ in range(m):
    r, c = map(int, input().split())
    balls[r-1][c-1] = 1

def moving_ball(row, col, copiedballs):
    max_value = 0
    max_row, max_col = -1, -1
    for direction in grid_direction:
        if in_range(row + direction[0], col + direction[1]) and max_value < grid[row + direction[0]][col + direction[1]]:
            max_value = grid[row + direction[0]][col + direction[1]]
            max_row = row + direction[0]
            max_col = col + direction[1]
    copiedballs[row][col] -= 1
    copiedballs[max_row][max_col] += 1

time = 0
while time < t:
    time += 1
    copied_balls = copy.deepcopy(balls)
    for row in range(n):
        for col in range(n):
            if balls[row][col] > 0:
                moving_ball(row, col, copied_balls)
    balls = copied_balls
    for row in range(n):
        for col in range(n):
            if balls[row][col] > 1: balls[row][col] = 0

count = 0
for row in range(n):
        for col in range(n):
            if balls[row][col] > 0: count += 1

print(count)