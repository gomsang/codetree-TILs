K, N = map(int, input().split())

answer = []

for _ in range(N):
    answer.append(1)

def choose(curr):
    print(*answer)

    if answer[-1] < K:
        answer[-1] += 1
        choose(curr)
    else:
        if answer[curr] < K:
            answer[curr] += 1
            answer[-1] = 1
            choose(curr) 
        elif curr > 0:
            choose(curr - 1)
            answer[-1] = 1

choose(N - 2)