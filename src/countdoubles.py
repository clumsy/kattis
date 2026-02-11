from collections import deque


n, m = (int(i) for i in input().split())
a = (int(i) for i in input().split())
cnt = [0] * 2
d = deque()
res = 0
for i, e in enumerate(a):
    if i >= m:
        cnt[(d.popleft()) & 1] -= 1
    d.append(e)
    cnt[e & 1] += 1
    if i > m - 1:
        res += cnt[0] > 1
print(res)
