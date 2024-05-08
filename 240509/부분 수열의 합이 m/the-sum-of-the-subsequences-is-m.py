import sys
INT_MAX = sys.maxsize

n, m = map(int, input().split())

A = list(map(int, input().split()))

dp = [INT_MAX] * (m + 1)
dp[0] = 0

for num in A:
    for j in range(m,num - 1, -1):
        if dp[j - num] != INT_MAX:
            dp[j] = min(dp[j], dp[j - num] + 1)

print(dp[m] if dp[m] != INT_MAX else -1)