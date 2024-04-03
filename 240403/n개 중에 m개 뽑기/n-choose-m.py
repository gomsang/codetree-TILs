M, N = map(int, input().split())

def calc(arr, offset):
    if len(arr) == N:
        print(*arr)
        return

    for i in range(offset, M + 1):
        calc(arr + [i], i + 1)

calc([], 1)