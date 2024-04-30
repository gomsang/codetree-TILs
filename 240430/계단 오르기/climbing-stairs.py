n = int(input())

dp = [-1] * (n + 1)

dp[0] = 1
if n >= 2:
    dp[2] = 1
if n >= 3:
    dp[3] = 1

def process(n):
    if n < 0:
        return 0
    if dp[n] > -1:
        return dp[n]
    dp[n] = process(n-2) + process(n-3)
    return dp[n]

if n >= 4:
    process(n)

print(dp[n] % 10007)

# n = int(input())

# dp = [0] * (n + 1)

# dp[0] = 1
# if n >= 2:
#  dp[2] = 1
# if n >= 3:
#  dp[3] = 1

# for i in range(4, n + 1):
#     if dp[i - 2] > 0:
#         dp[i] += dp[i - 2]
#     if dp[i - 3] > 0:
#         dp[i] += dp[i - 3]

# print(dp[n] % 10007)