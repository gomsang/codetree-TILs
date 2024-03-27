import copy

move = [(0, 1), (1, 0), (0, -1), (-1, 0)]

# 우 하 좌 상
direction = 0

n = int(input())
x, y = map(int, input().split())

grid = []

for row in range(n):
    grid.append(list(input()))


def rotate_left():
    global direction
    direction = (direction - 1) % 4


def rotate_right():
    global direction
    direction = (direction + 1) % 4


def is_move_position_is_wall(x, y, direction):
    # 벗어남 (탈출)
    if not ((0 <= (x + move[direction][0]) - 1 < n) and (0 <= (y + move[direction][1]) - 1 < n)):
        return False
    if grid[(x + move[direction][0]) - 1][(y + move[direction][1]) - 1] == "#":
        return True
    return False


def is_move_position_is_escape(x, y, direction):
    # 벗어남 (탈출)
    if not ((0 <= (x + move[direction][0]) - 1 < n) and (0 <= (y + move[direction][1]) - 1 < n)):
        return True
    return False


def is_move_position_right_side_wall(x, y, direction):
    if not ((0 <= (x + move[direction][0] + move[(direction + 1) % 4][0]) - 1 < n) and (
            0 <= (y + move[direction][1] + move[(direction + 1) % 4][1]) - 1 < n)):
        return False
    if grid[
        (x + move[direction][0] + move[(direction + 1) % 4][0]) - 1][
        (y + move[direction][1] + move[(direction + 1) % 4][1]) - 1] == "#":
        return True
    return False


def print_direction(x, y, direction):
    # 방향에 따른 화살표 기호를 정의합니다.
    arrows = ['→', '↓', '←', '↑']

    # grid의 복사본을 만듭니다.
    copied = copy.deepcopy(grid)

    # 주어진 위치와 방향에 맞는 화살표 기호를 넣습니다.
    # x와 y는 1부터 시작하는 위치를 가정합니다.
    copied[y - 1][x - 1] = arrows[direction]

    print("---------------------------")
    # 결과 grid를 출력합니다.
    for row in copied:
        print(' '.join(row))


isocnt = 0
t = 0
while (True):
    # print_direction(x, y, direction)
    if isocnt >= 4:
        t = -1
        break
    if is_move_position_is_wall(x, y, direction):
        rotate_left()
        isocnt += 1
    elif is_move_position_is_escape(x, y, direction):
        t += 1
        break
    else:
        isocnt = 0
        if is_move_position_right_side_wall(x, y, direction):
            x = x + move[direction][0]
            y = y + move[direction][1]
            t += 1
        else:
            x = x + move[direction][0]
            y = y + move[direction][1]
            t += 1
            rotate_right()
            x = x + move[direction][0]
            y = y + move[direction][1]
            t += 1
    if t >= n * n:
        t = -1
        break

print(t)