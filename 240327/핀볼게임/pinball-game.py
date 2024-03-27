N = int(input())

grid = []

direction_coord = {
    'L': (0, -1),
    'R': (0, 1),
    'U': (-1, 0),
    'D': (1, 0),
}

for _ in range(N):
    grid.append(list(map(int, input().split())))


def simulate(row, col, direction):
    t = 1
    while (0 <= row < N) and (0 <= col < N):
        if grid[row][col] == 1:
            if direction == 'D':
                direction = 'L'
            elif direction == 'U':
                direction = 'R'
            elif direction == 'R':
                direction = 'U'
            elif direction == 'L':
                direction = 'D'
        elif grid[row][col] == 2:
            if direction == 'D':
                direction = 'R'
            elif direction == 'U':
                direction = 'L'
            elif direction == 'R':
                direction = 'D'
            elif direction == 'L':
                direction = 'U'
        row += direction_coord[direction][0]
        col += direction_coord[direction][1]
        t += 1
    return t


max_t = 0
for col in range(N):
    max_t = max(max_t, simulate(0, col, 'D'), simulate(N - 1, col, 'U'))

for row in range(N):
    max_t = max(max_t, simulate(row, 0, 'R'), simulate(row, N - 1, 'L'))

print(max_t)