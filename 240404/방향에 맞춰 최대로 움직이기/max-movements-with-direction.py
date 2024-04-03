n = int(input())
directions = [(1,0), (1,1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (-1, -1)]

grid_numbers = []
grid_directions = []

moving_trace = []

for _ in range(n):
    grid_numbers.append(list(map(int, input().split())))


for _ in range(n):
    grid_directions.append(list(map(int, input().split())))

r, c = map(int, input().split())

def get_availables(r, c):
    direction = grid_directions[r][c] - 1
    step = 1
    moving_availables = []
    while (0 <= r + directions[direction][0] * step < n  and 0 <= r + directions[direction][1] * step < n) and grid_numbers[r][c] < grid_numbers[directions[direction][0] * step][r + directions[direction][1] * step]:
        moving_availables.append((r + directions[direction][0] * step, r + directions[direction][1] * step))
        step += 1
    return moving_availables

max_moving = 0

def traverse(r, c):
    global max_moving
    moving_availables = get_availables(r, c)
    if not moving_availables:
        max_moving = max(max_moving, len(moving_trace))
        return
    for (mr, mc) in moving_availables:
        moving_trace.append((mr, mc))
        traverse(mr, mc)
        moving_trace.pop()

traverse(r - 1, c - 1)
print(max_moving)