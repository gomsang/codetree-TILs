grid = []

def shift_left():
    for row in range(4):
        r = [n for n in grid[row] if n > 0]

        for i in range(len(r) - 1):
            if r[i] == r[i+1]:
                r[i] = r[i] + r[i+1]
                r[i + 1] = 0

        r = [n for n in r if n > 0]
        r.extend([0] * (4 - len(r)))
        grid[row] = r

def shift_right():
    for row in range(4):
        grid[row].reverse()
    shift_left()
    for row in range(4):
        grid[row].reverse()

def shift_up():
    global grid
    grid = [row for row in zip(*grid)]
    shift_left()
    grid = [row for row in zip(*grid)]

def shift_down():
    global grid
    grid = [row for row in zip(*grid)]
    shift_right()
    grid = [row for row in zip(*grid)]


for _ in range(4):
    grid.append(list(map(int, input().split())))

command = input()

if command == 'L':
    shift_left()
elif command == 'R':
    shift_right()
elif command == 'U':
    shift_up()
else:
    shift_down()

for row in grid:
    print(*row)