n, m = (int(i) for i in input().split())
res = ["?"] * n
for _ in range(m):
    s, d = input().split()
    s = int(s) - 1
    for i in range(len(d)):
        if res and res[s + i] == "?":
            res[s + i] = d[i]
        elif res and res[s + i] != d[i]:
            res = None
res = "".join(res) if res else "Villa"
print(res)
