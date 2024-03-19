N = int(input())

grid = []


def calc(srow, scol):
    calc = 0
    for r in range(3):
        for c in range(3):
            calc += grid[srow + r][scol + c]
    return calc


for i in range(N):
    # row = map(int, input().split())
    row = [int(num) for num in input().split()]
    grid.append(row)

coin = 0
for row in range(N - 2):
    for col in range(N - 2):
        coin = max(coin, calc(row, col))

print(coin)