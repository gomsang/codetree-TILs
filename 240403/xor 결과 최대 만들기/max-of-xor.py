N, M = map(int, input().split())
numbers = list(map(int, input().split()))

xor_max = 0

def calc(arr, offset):
    global xor_max
    if len(arr) == M:
        v = numbers[arr[0] - 1]
        for num in range(1, M):
            v = v ^ numbers[arr[num] - 1]
        xor_max = max(xor_max, v)
        return

    for i in range(offset, N + 1):
        calc(arr + [i], i + 1)

calc([], 1)
print(xor_max)