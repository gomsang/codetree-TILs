N, M = map(int, input().split())

bombs = []

def get_targets():
    lst = []
    last = 0
    for bi in range(1, len(bombs)):
        if bombs[bi - 1] != bombs[bi]:
            lst.append((last, bi - 1))
            last = bi

    lst.append((last, len(bombs) - 1))
    lst = [coord for coord in lst if (coord[1] - coord[0] + 1) >= M]
    return lst

def fire(targets):
    global bombs
    result = []
    for bi in range(len(bombs)):
        if not targets or not targets[0][0] <= bi <= targets[0][1]:
            result.append(bombs[bi])
        if targets and bi >= targets[0][1]:
            targets.pop(0)
    bombs = result


for _ in range(N):
    bombs.append(int(input()))

while(True):
    targets = get_targets()
    if targets:
        fire(targets)
    else:
        break

print(len(bombs))
for b in bombs:
    print(b)