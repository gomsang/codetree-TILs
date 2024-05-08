import sys

INT_MAX = sys.maxsize

N, M = map(int, input().split())
dp = [INT_MAX] * (M + 1)
dp[0] = 0
coin = list(map(int, input().split()))

for i in range(1, M + 1):
    for j in range(N):
        if i - coin[j] >= 0:
            if dp[i - coin[j]] == INT_MAX:
                continue

            dp[i] = min(dp[i], dp[i - coin[j]] + 1) 

print(-1 if dp[M] == INT_MAX else dp[M])