n = int(input())
visited = [False] * n

def visit(arr):
    if len(arr) == n:
        print(*arr)
        return
    for v in range(n - 1, -1, -1):
        if not visited[v]:
            visited[v] = True
            visit(arr + [v + 1])
            visited[v] = False

for num in range(n - 1, -1, -1):
    visited[num] = True
    visit([num + 1])
    visited[num] = False