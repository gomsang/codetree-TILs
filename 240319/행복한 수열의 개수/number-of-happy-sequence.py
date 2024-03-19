N, M = map(int, input().split())

grid = []

for row in range(N):
    grid.append(list(map(int, input().split())))

cnt = 0

# 가로 줄 계산
for row in range(N):
    current_row_max = 1
    score = 1
    for col in range(1, N):
        if grid[row][col - 1] == grid[row][col]:
            score += 1
            current_row_max = max(current_row_max, score)
        else:
            score = 1
    if current_row_max >= M:
        cnt += 1

# 세로 줄 계산
for col in range(N):
    current_col_max = 1
    score = 1
    for row in range(1, N):
        if grid[row - 1][col] == grid[row][col]:
            score += 1
            current_col_max = max(current_col_max, score)
        else:
            score = 1
    if current_col_max >= M: cnt += 1

print(cnt)