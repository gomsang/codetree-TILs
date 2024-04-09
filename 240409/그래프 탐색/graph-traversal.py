N, M = map(int, input().split())

graph = [[] for _ in range(N + 1)]

visited = [False for _ in range(N + 1)]

def dfs(vertex):
    for curr_v in graph[vertex]:
        if not visited[vertex]:
            visited[vertex] = True
            dfs(curr_v)


for _ in range(M):
    x, y = map(int, input().split())
    graph[x].append(y)

dfs(1)
visited[1]

print(sum(visited))