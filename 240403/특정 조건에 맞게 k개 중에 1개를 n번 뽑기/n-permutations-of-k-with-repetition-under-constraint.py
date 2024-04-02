K, N = map(int,input().split())

def choose(arr):
    if len(arr) == N:
        print(*arr)
        return
    else:
        for num in range(1, K + 1):
            if not (len(arr) > 1 and arr[-2] == arr[-1] and arr[-1] == num):
                choose(arr + [num])

choose([])