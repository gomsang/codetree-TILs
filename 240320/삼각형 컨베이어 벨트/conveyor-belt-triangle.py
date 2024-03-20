n, t = map(int, input().split())

belt = []

belt += list(map(int, input().split()))
belt += list(map(int, input().split()))
belt += list(map(int, input().split()))

t = 3 * n - (t % (3 * n))
belt *= 3

print(*belt[t:t+n])
print(*belt[t+n:t+2*n])
print(*belt[t+2*n:t+3*n])