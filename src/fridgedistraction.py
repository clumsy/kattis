from string import ascii_lowercase
from collections import deque

k, n = (int(i) for i in input().split())
q = deque(ascii_lowercase[:k])
res = []
while n:
    if n >= k:
        res.append(q.pop())
        q.appendleft(res[-1])
        n -= k
    else:
        res.append(q[n - 1])
        n = 0
print(len(res))
res = " ".join(res)
print(res)
