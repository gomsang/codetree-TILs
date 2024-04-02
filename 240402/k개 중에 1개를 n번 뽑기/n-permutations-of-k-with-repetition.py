K, N = map(int, input().split())

answer = []


def choose(arr):
    if len(arr) == N:
        print(*arr)
        return
    for num in range(1, K + 1):
        choose(arr + [num])


choose([])