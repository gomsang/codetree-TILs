n = int(input())
visited = [False] * n

def visit(arr):
    if len(arr) == n:
        print(*arr)
        return
    for v in range(n):
        if not visited[v]:
            visited[v] = True
            visit(arr + [v + 1])
            visited[v] = False

for num in range(n):
    visited[num] = True
    visit([num + 1])
    visited[num] = False