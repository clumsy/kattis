n, k = (int(i) for i in input().split())
res = 0
for _ in range(n):
    s = input().split()
    res += k - len(set(s))
print(res)
