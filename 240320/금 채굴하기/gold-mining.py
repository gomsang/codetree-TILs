N, M = map(int, input().split())

grid = []

coord_gold = []


def dig(row, col, k):
    num = 0
    for x, y in coord_gold:
        if abs(row - x) + abs(col - y) <= k:
            num += 1
    return num


for _ in range(N):
    grid.append(list(map(int, input().split())))

for row in range(N):
    for col in range(N):
        if grid[row][col] == 1:
            coord_gold.append([row, col])

gold = 0

for row in range(N):
    for col in range(N):
        for k in range(N):
            dig_gold = dig(row, col, k)
            if M * dig_gold >= k * k + (k + 1) * (k + 1):
                gold = max(gold, dig_gold)

print(gold)