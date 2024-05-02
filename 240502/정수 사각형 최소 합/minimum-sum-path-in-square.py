n = int(input())

a = []

for i in range(n):
    a.append(list(map(int, input().split())))

dp = [
    [0 for _ in range(n)] for _ in range(n)
]

dp[0][n-1] = a[0][n-1]

for i in range(n-2, -1, -1):
    dp[0][i] = dp[0][i+1] + a[0][i]

for i in range(1, n):
    dp[i][n-1] = dp[i-1][n-1] + a[i][n-1]

for i in range(1, n):
    for j in range(n-2, -1, -1):
        dp[i][j] = min(dp[i][j+1] + a[i][j], dp[i-1][j] + a[i][j])

print(dp[n-1][0])