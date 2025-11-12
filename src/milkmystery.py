from collections import deque


n, k = (int(i) for i in input().split())
d = (int(i) for i in input().split())
res = cur = 0
h = deque()
for i in d:
    cur += i
    h.append(i)
    if len(h) > k:
        cur -= h.popleft()
    res = max(res, cur)
print(res)
