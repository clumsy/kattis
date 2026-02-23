from collections import deque


h, w = (int(i) for i in input().split())
m = [list(input()) for _ in range(h)]

q = deque([(r, c) for r in range(h) for c in range(w) if m[r][c] == "S"])
cur = 0
res = "thralatlega nettengdur"
while q:
    for _ in range(len(q)):
        r, c = q.popleft()
        if m[r][c] == "G":
            res = cur
            q.clear()
            break
        elif m[r][c] != "#":
            m[r][c] = "#"
            if r > 0:
                q.append((r - 1, c))
            if c > 0:
                q.append((r, c - 1))
            if r < h - 1:
                q.append((r + 1, c))
            if c < w - 1:
                q.append((r, c + 1))
    cur += 1
print(res)
