n, m = (int(input()) for _ in range(2))
s = input().split()
cnt = [0] * n
for _ in range(m):
    vs = (int(i) for i in input().split())
    for i, v in enumerate(vs):
        cnt[i] += v
ma = max(cnt)
i = next(i for i, v in enumerate(cnt) if v == ma)
res = s[i]
print(res)
