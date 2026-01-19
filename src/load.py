n = int(input())
ks, ws = [], []
for _ in range(n):
    k, m, w = (int(i) for i in input().split())
    ks.append(k * m)
    ws.append(w)
res = sum(ki * wi for ki, wi in zip(sorted(ks), sorted(ws)))
print(res)
