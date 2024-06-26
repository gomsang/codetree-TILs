n = int(input())

dp = [0] * (n+1)

dp[0] = 1


for i in range(1, n + 1):
    if i >= 1:
        dp[i] = (dp[i] + dp[i - 1])
    if i >= 2:
        dp[i] = (dp[i] + dp[i - 2])
    if i >= 5:
        dp[i] = (dp[i] + dp[i - 5])

print(dp[n] % 10007)

# dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 5]