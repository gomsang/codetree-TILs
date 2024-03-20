n, t = map(int, input().split())

belt = []

belt += list(map(int, input().split()))
belt += list(map(int, input().split()))

t = 2 * n -t % (2 * n)
belt += belt

print(*belt[t:t+n])
print(*belt[t+n:t+2*n])