import sys
INT_MAX = sys.maxsize

n, m = map(int, input().split())

A = list(map(int, input().split()))

dp = [INT_MAX] * (m + 1)

for i in range(1, n + 1):
    for j in range(m, -1, -1):
        if dp[j - i] != INT_MAX:
            dp[i] = min(dp[i], dp[j - i] + 1)

print(dp[m] if dp[m] != INT_MAX else -1)