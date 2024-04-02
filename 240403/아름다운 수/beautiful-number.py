n = int(input())

cnt = 0
def choose(text):
    global cnt
    if len(text) > 0:
        cnt = cnt + 1
    for num in range(1, n - len(text) + 1):
        choose(text + str(num) * num)

choose("")
print(cnt)