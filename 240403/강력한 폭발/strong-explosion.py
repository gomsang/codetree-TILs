n = int(input())

grid = []

directions = [
    [(-2, 0), (-1, 0), (1, 0), (2, 0)],
    [(-1, 0), (0, 1), (1, 0), (0, -1)],
    [(-1, -1), (-1, 1), (1, 1), (1, -1)]
]

for row in range(n):
    grid.append(list(map(int, input().split())))

bombcnt = 0

for row in range(n):
    for col in range(n):
        if grid[row][col] == 1:
            bombcnt += 1

def score(bombs):
    scoregrid = [[0 for _ in range(n)] for _ in range(n)]
    for row in range(n):
        for col in range(n):
            if grid[row][col] > 0:
                bombtype = bombs.pop(0)
                scoregrid[row][col] = 1
                for direction in directions[bombtype - 1]:
                    if 0 <= row + direction[0] < n and 0 <= col + direction[1] < n:
                        scoregrid[row + direction[0]][col + direction[1]] = 1
    scoresum = 0
    for row in range(n):
        for col in range(n):
            if scoregrid[row][col] > 0:
                scoresum += 1
    return scoresum

scoremax = 0

def traverse(bombs):
    global scoremax
    if len(bombs) == bombcnt:
        scoremax = max(scoremax, score(bombs))
        return
    for bombtype in range(1,4):
        traverse(bombs + [bombtype])

traverse([])

print(scoremax)