n = int(input())
segments = []
for _ in range(n):
    x1, x2 = map(int, input().split())
    segments.append((x1, x2))

selected_segments = list()

def is_overlap(segment1, segment2):
    (ax1, ax2), (bx1, bx2) = segment1, segment2
    return (ax1 <= bx1 <= ax2) or (ax1 <= bx2 <= ax2) or (bx1 <= ax1 <= bx2) or (bx1 <= ax2 <= bx2)

def possible():
    for idx_a, segment1 in enumerate(selected_segments):
            for idx_b, segment2 in enumerate(selected_segments):
                if idx_a < idx_b and is_overlap(segment1, segment2):
                    return False
    return True

selectmax = 0

def check(idx):
    global selectmax
    if select == n:
        if possible():
            selectmax = max(selectmax, len(selected_segments))
        return
    
    selected_segments.append(segments[idx])
    check(idx + 1)
    selected_segments.pop()
    check(idx + 1)

check(0)
print(selectmax)