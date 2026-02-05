n = int(input())
r = {}


def add(s):
    c = r
    for d in s:
        if d not in c:
            c[d] = {"cnt": 0}
        c[d]["cnt"] += 1
        c = c[d]


for _ in range(n):
    s = input()
    add(s)

c = r
res = []
while n:
    d = "0" if c.get("0", {}).get("cnt", 0) <= c.get("1", {}).get("cnt", 0) else "1"
    res.append(d)
    c = c.get(d, {})
    n -= 1
res = "".join(res)
print(res)
