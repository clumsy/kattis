n, s = (int(i) for i in input().split())
for _ in range(n):
    l, r = (int(i) for i in input().split())
    s += l <= s <= r
res = s
print(res)
