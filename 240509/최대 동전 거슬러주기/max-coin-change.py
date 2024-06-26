import sys

INT_MIN = -sys.maxsize

N, M = map(int, input().split())

coins = list(map(int, input().split()))

dp = [INT_MIN] * (M + 1)
dp[0] = 0

for coin in coins:
    for j in range(coin, M + 1):
        if dp[j - coin] == INT_MIN:
            continue
        dp[j] = max(dp[j], dp[j - coin] + 1)

print(dp[M] if dp[M] != INT_MIN else -1)