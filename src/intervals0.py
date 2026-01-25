n, k = (int(i) for i in input().split())
h = [0] * 24
for _ in range(n):
    b, e = (int(i) for i in input().split())
    h[b] += 1
    h[e] -= 1
res = cur = 0
for i in h:
    cur += i
    res += cur >= k
print(res)
