n = int(input())

blocks = []

def delblock(start, end):
    modified = []
    for bi in range(len(blocks)):
        if not start - 1 <= bi <= end -1:
            modified.append(blocks[bi])
    return modified

for _ in range(n):
    blocks.append(int(input()))

s, e = map(int, input().split())
blocks = delblock(s, e)
s, e = map(int, input().split())
blocks = delblock(s,e)

print(len(blocks))
for block in blocks:
    print(block)