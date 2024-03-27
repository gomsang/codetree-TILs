n, m, row, col = map(int, input().split())
directions = input().split()
directions.append("N")

dice_top = 1
dice_front = 2
dice_right = 3

grid = [[-1 for _ in range(n)] for _ in range(n)]


def dice(direction):
    global dice_top, dice_front, dice_right
    if direction == 'L':
        dice_top, dice_right = dice_right, 7 - dice_top
    elif direction == 'R':
        dice_top, dice_right = 7 - dice_right, dice_top
    elif direction == 'U':
        dice_top, dice_front = dice_front, 7 - dice_top
    elif direction == 'D':
        dice_top, dice_front = 7 - dice_front, dice_top


direction_coord = {
    'L': (0, -1),
    'R': (0, 1),
    'U': (-1, 0),
    'D': (1, 0),
    'N': (0, 0)
}

grid[row - 1][col - 1] = (7 - dice_top)
sum_point = (7 - dice_top)

for direction in directions:
    if 1 <= row + direction_coord[direction][0] <= n and 1 <= col + direction_coord[direction][1] <= n:
        row += direction_coord[direction][0]
        col += direction_coord[direction][1]
        if grid[row - 1][col - 1] != -1:
            sum_point -= grid[row - 1][col - 1]
        dice(direction)
        sum_point += (7 - dice_top)
        grid[row - 1][col - 1] = (7 - dice_top)

print(sum_point)