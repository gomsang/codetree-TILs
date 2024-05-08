n, m = map(int, input().split())
A = list(map(int, input().split()))

dp = [False] * (m + 1)
dp[0] = True

for num in A:
    for j in range(m, num - 1, -1):
        if dp[j - num]:
            dp[j] = True

print("Yes" if dp[m] else "No")