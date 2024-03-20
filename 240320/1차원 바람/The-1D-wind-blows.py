N, M, Q = map(int, input().split())

grid = []

for _ in range(N):
    grid.append(list(map(int, input().split())))

def isInfectionEnable(lstA, lstB):
    for (A, B) in zip(lstA, lstB):
        if A == B:
            return True
    return False

def hoo(row, direction, enable_infection_up, enable_infection_down):
    if direction == 'L':
        grid[row] = [grid[row][-1]] + grid[row][:-1]
    elif direction == 'R':
        grid[row] = grid[row][1:] + [grid[row][0]]
    
    if(enable_infection_up and row > 0 and isInfectionEnable(grid[row], grid[row - 1])):
        hoo(row - 1, 'R' if  direction == 'L' else 'L', True, False)
    if(enable_infection_down and row < N - 1 and isInfectionEnable(grid[row], grid[row + 1])):
        hoo(row + 1,'R' if  direction == 'L' else 'L', False, True)

for _ in range(Q):
    row, direction = input().split()
    row = int(row)
    hoo(row - 1, direction, True, True)

for row in grid:
    print(*row)