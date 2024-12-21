cnt = {}
for f in range(1, 7):
    for s in range(1, 7):
        cnt[f + s] = cnt.get(f + s, 0) + 1
n = int(input())
a = (int(i) for i in input().split())
res = sum(cnt[i] for i in a) / sum(cnt.values())
print(res)
