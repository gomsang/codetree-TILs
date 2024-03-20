import copy
n = int(input())

grid = []

direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]

max_score = 0

def calc(row, col):
    global max_score
    cloned_grid = copy.deepcopy(grid)

    power = cloned_grid[row - 1][col - 1]
    cloned_grid[row - 1][col - 1] = 0

    # 가로 축
    for c in range(max(0, (col - 1) - (power - 1)), min(n, (col - 1) + (power - 1) + 1)):
        cloned_grid[row - 1][c] = 0

    # 세로 축
    for r in range(max(0, (row - 1) - (power - 1)), min(n, (row - 1) + (power - 1) + 1)):
        cloned_grid[r][col - 1] = 0

    for c in range(n):
        lst = []
        for r in range(n):
            if cloned_grid[r][c] > 0:
                lst.append(cloned_grid[r][c])

        for r in range(n - 1, -1, -1):
            if lst:
                cloned_grid[r][c] = lst.pop()
            else:
                cloned_grid[r][c] = 0

    sum_score = 0
    for r in range(n):
        for c in range(n):
            score = 0
            if cloned_grid[r][c] == 0: continue
            if c < (n - 1) and cloned_grid[r][c] == cloned_grid[r][ c + 1]:
                score += 1
            if r < (n - 1) and cloned_grid[r][c] == cloned_grid[r + 1][c]:
                score += 1
            sum_score += score
    max_score = max(max_score, sum_score)


for _ in range(n):
    grid.append(list(map(int, input().split())))

for row in range(1, n + 1):
    for col in range(1, n + 1):
        calc(row, col)


print(max_score)