N, M, K = map(int, input().split())

max_score = 0

def game(locates, distances):
    global max_score
    if not distances:
        score = 0
        for locate in locates:
            if locate >= M:
                score += 1
        max_score = max(max_score, score)
        return

    distances_cpy = distances[:]
    distance = distances_cpy.pop(0)

    for k in range(K):
        locates_cpy = locates[:]
        locates_cpy[k] += distance
        game(locates_cpy, distances_cpy)

game([1 for _ in range(K)], list(map(int, input().split())))
print(max_score)