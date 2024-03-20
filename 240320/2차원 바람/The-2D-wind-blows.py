import copy

N, M, Q = map(int, input().split())


grid = []

directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def create_top(r1, c1, r2, c2):
    top = grid[r1][c1: c2]
    return top


def apply_top(top, r1, c1, r2, c2):
    for t in range(len(top)):
        grid[r1][c1 + t] = top[t]


def create_bottom(r1, c1, r2, c2):
    bottom = grid[r2][c1 + 1: c2 + 1]
    return bottom


def apply_bottom(bottom, r1, c1, r2, c2):
    for t in range(len(bottom)):
        grid[r2][c1 + 1 + t] = bottom[t]


def create_left(r1, c1, r2, c2):
    left = []
    for row in range(r1 + 1, r2 + 1):
        left.append(grid[row][c1])
    return left


def apply_left(left, r1, c1, r2, c2):
    for l in range(len(left)):
        grid[r1 + 1 + l][c1] = left[l]


def create_right(r1, c1, r2, c2):
    right = []
    for row in range(r1, r2):
        right.append(grid[row][c2])
    return right


def apply_right(right, r1, c1, r2, c2):
    for r in range(len(right)):
        grid[r1 + r][c2] = right[r]


def calc_avg(row, col):
    global clone_grid
    sum = clone_grid[row][col]
    cnt = 1
    for direction in directions:
        drow, dcol = row + direction[0], col + direction[1]
        if 0 <= drow < N and 0 <= dcol < M:
            sum += clone_grid[drow][dcol]
            cnt += 1
    return sum // cnt


for _ in range(N):
    grid.append(list(map(int, input().split())))

for _ in range(Q):
    r1, c1, r2, c2 = map(int, input().split())

    top = create_top(r1 - 1, c1 - 1, r2 - 1, c2 - 1)
    bottom = create_bottom(r1 - 1, c1 - 1, r2 - 1, c2 - 1)
    left = create_left(r1 - 1, c1 - 1, r2 - 1, c2 - 1)
    right = create_right(r1 - 1, c1 - 1, r2 - 1, c2 - 1)

    tmp = left[0]
    left = left[1:] + [bottom[0]]
    bottom = bottom[1:] + [right[-1]]
    right = [top[-1]] + right[:-1]
    top = [tmp] + top[:-1]

    apply_top(top, r1 - 1, c1 - 1, r2 - 1, c2 - 1)
    apply_bottom(bottom, r1 - 1, c1 - 1, r2 - 1, c2 - 1)
    apply_left(left, r1 - 1, c1 - 1, r2 - 1, c2 - 1)
    apply_right(right, r1 - 1, c1 - 1, r2 - 1, c2 - 1)

    clone_grid = copy.deepcopy(grid)

    for row in range(r1 - 1, r2):
        for col in range(c1 - 1, c2):
            grid[row][col] = calc_avg(row, col)

for row in grid:
    print(*row)