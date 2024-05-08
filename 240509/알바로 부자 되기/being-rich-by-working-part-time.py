N = int(input())
jobs = [list(map(int,input().split())) for _ in range(N)]

dp = [0] * N

for i in range(N):
    dp[i] = jobs[i][2]

for i in range(1, N):
    job_p = jobs[i][2]
    prev_p = 0
    for j in range(i):
        if jobs[j][1] < jobs[i][0]:
            prev_p = max(prev_p, dp[j])
    dp[i] = job_p + prev_p

print(max(dp))