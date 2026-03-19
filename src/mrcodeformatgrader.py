c, n = (int(i) for i in input().split())
ls = (int(i) for i in input().split())
es, cs = [], []
b = p = None
for cur in ls:
    if not b:
        b = cur
        if b > 1:
            cs.append("1" if b == 2 else f"1-{b - 1}")
    elif cur - p > 1:
        es.append(f"{b}" if b == p else f"{b}-{p}")
        cs.append(f"{cur - 1}" if cur - p == 2 else f"{p + 1}-{cur - 1}")
        b = cur
    p = cur
if b:
    es.append(f"{b}" if b == p else f"{b}-{p}")
    if p + 1 <= c:
        cs.append(f"{p + 1}" if p + 1 == c else f"{p + 1}-{c}")
if len(es) > 1:
    p1, p2 = es.pop(), es.pop()
    es.append(f"{p2} and {p1}")
es = ", ".join(es)
if len(cs) > 1:
    p1, p2 = cs.pop(), cs.pop()
    cs.append(f"{p2} and {p1}")
cs = ", ".join(cs)
res = f"Errors: {es}\nCorrect: {cs}"
print(res)
