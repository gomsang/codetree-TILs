text = input()

def rl():
    ch = text[0]
    cnt = 1
    result = ""
    for i in range(1, len(text)):
        if text[i - 1] == text[i]:
            cnt += 1
        else:
            result += ch + str(cnt)
            ch = text[i]
            cnt = 1
    result += ch + str(cnt)
    return len(result)


short = rl()

for _ in range(len(text) - 1):
    text = text[-1] + text[:-1]
    short = min(short, rl())

print(short)