N, M = map(int, input().split())

grid = []

negative_numbers = []

for _ in range(N):
    grid.append(list(map(int, input().split())))

for row in range(N):
    for col in range(M):
        if grid[row][col] < 0:
            negative_numbers.append([row, col])


def having_negative(s_row, s_col, e_row, e_col):
    for n_row, n_col in negative_numbers:
        if s_row <= n_row <= e_row and s_col <= n_col <= e_col:
            return True
    return False


def check(width, height):
    for grid_row in range(N - height + 1):
        for grid_col in range(M - width + 1):
            if not having_negative(grid_row, grid_col, grid_row + height - 1, grid_col + width - 1):
                return True
    return False


def run():
    if not negative_numbers:
        return N * M

    score = -1
    for w in range(1, M + 1):
        for h in range(1, N + 1):
            if check(w, h):
                score = max(score, w * h)
    return score


print(run())