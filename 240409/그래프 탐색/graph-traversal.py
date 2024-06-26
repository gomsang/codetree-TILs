N, M = map(int, input().split())

graph = [[] for _ in range(N + 1)]

visited = [False for _ in range(N + 1)]

def dfs(vertex):
    for curr_v in graph[vertex]:
        if not visited[curr_v]:
            visited[curr_v] = True
            dfs(curr_v)


for _ in range(M):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

dfs(1)
visited[1] = True

print(sum(visited) - 1)