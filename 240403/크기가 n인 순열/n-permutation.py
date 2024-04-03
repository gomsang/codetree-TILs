n = int(input())
visited = [False] * n

def visit(arr, pos):
    if len(arr) == n:
        print(*arr)
        return
    for v in range(n):
        if not visited[v]:
            visited[v] = True
            visit(arr + [v + 1], v)
            visited[v] = False

for num in range(n):
    visited[num] = True
    visit([num + 1], num)
    visited[num] = False