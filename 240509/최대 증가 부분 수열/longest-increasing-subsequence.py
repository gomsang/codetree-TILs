N = int(input())
arr = list(map(int, input().split()))

dp = [0] * N

for i in range(1, N):
    for j in range(i):
        if arr[j] < arr[i]:
            dp[i] = max(dp[i], dp[i] + 1)

print(max(dp))